# chatbotPythonReact
This project implements a voice-enabled chatbot using a combination of Python, FastAPI, React, and TypeScript. It leverages ChatGPT for natural language processing and text-to-speech conversion for a seamless voice interaction experience.

# Prerequisites:
Python 3.x (https://www.python.org/downloads/)
Node.js and npm (https://nodejs.org/)


# Set up API keys:
Create a file named .env in the project's Backend folder (.env is typically ignored by Git to prevent accidental key exposure).
Add the following lines to .env, replacing the placeholders with your actual API keys:

OPEN_AI_ORG=your_openai_org
OPEN_AI_KEY=your_openai_key
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key

# to Run
  ## backend 
  uvicorn main:app
  ## Frontend
  yarn dev
  
# Functionality
User interacts with the chatbot through voice input.
User's voice input is sent to the backend server for processing.
The backend utilizes ChatGPT's API for natural language understanding and generates a response.
The generated response from ChatGPT is converted to audio using a text-to-speech library in the backend (e.g., ElevenLabs API).
The synthesized audio is then sent back to the frontend and played for the user.
The user can continue interacting with the chatbot in this voice-driven manner.
Note: Depending on the specific libraries used for text-to-speech conversion, additional configuration or paid API plans might be necessary.
