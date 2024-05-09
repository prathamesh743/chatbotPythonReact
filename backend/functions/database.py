from email import message
import  json
import random 

# get recent megs
def get_recent_msgs():
    #define file name and learn instructions 
    file_name = "stored_data.json"
    learn_instruction = {
        "role":"system",
        "content":"you are interviewing user for job as retail assistant ask relevant questions .your name is Rachel, keep your answer to under 15 words"
    }

    #init msgs
    messages = []

    #random  element
    x= random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + ", add humour to response."
    else:
        learn_instruction["content"] = learn_instruction["content"] + ", add leading question to response."
    
    #append messages
    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)    
                else:
                    for item in data[-5:]:
                        messages.append(item)


    except Exception as e:
        pass    
    return messages

#
def store_messages(request_message,response_message):
    #define file name 
    file_name = "stored_data.json"

    messages = get_recent_msgs()[1:]

    #add messages to data
    user_message =  {"role":"user","content":request_message}
    assistant_message =  {"role":"assistant","content":response_message}

    messages.append(user_message)
    messages.append(assistant_message)

    #save updated file 
    with open(file_name,"w") as f:
        json.dump(messages,f)


#reset messages 
def reset_msgs():
    open("stored_data.json","w")        