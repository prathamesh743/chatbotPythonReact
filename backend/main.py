# uvicorn main:app --reload
# uvicorn main:app
# venv/Scripts/activate 

#main import
from email.mime import audio
import http
from fastapi import FastAPI, File, UploadFile , HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import Config
import openai


# custom function imports
from functions.openai_requests import convert_audio_to_text,get_chat_response
from functions.database import store_messages,reset_msgs
from functions.text_to_speech import convert_text_to_speech
# initiate app
app = FastAPI()

#cors - origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://localhost:4173"
]

# cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers =["*"],
                   
                   )



#check 
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

#check 2 
@app.get("/reset")
async def reset_conversation():
    reset_msgs()
    return {"message": "conversation cleared"}


#get
@app.post("/post-audio/")
async def post_audio(file:UploadFile = File(...)):
    # audio_input = open("voice.mp3","rb")

    #save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())
    
    audio_input = open(file.filename,"rb")
    
    #decode
    message_decoded = convert_audio_to_text(audio_input)
    #check -ensure msg decoded
    if not message_decoded:
        return HTTPException(status_code=400,detail="failed to decode audio")
        
    #get chatgpt response
    chat_response = get_chat_response(message_decoded)
    if not chat_response:
        return HTTPException(status_code=400,detail="failed to get chat  response")
    
    #store messages
    store_messages(message_decoded,chat_response)

    #convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400,detail="failed to get audio response")
    
    
    #generator for chunks of data
    def iterfile():
        yield audio_output

    #return audio file
    return StreamingResponse(iterfile(),media_type="application/octet-stream")



