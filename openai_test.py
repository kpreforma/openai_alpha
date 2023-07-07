from dotenv.main import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.environ['OPEN_AI_API_KEY']

def openai_response(input_message, system_message):
    messages = []
    messages.append({
        "role": "system",
        "content": system_message
    })
    
    messages.append({
        "role":"user",
        "content": input_message})

    print(messages)

    response = openai.ChatCompletion.create(
        model = os.environ['OPEN_AI_MODEL'],
        messages = messages
    )

    return response