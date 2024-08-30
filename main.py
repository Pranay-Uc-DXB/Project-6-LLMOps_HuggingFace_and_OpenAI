# %%
# !pip install fastapi
# # !pip install uvicorn[standard]

import sys
sys.path.append('venv1\Project_files\config.py')



from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import config
import os

api_key= os.environ['OPENAI_API']
assistant_id= config.assistant_id

Assistant_key=assistant_id
client= OpenAI(api_key=api_key)


app=FastAPI()

# Defining input string format to be parsed from the user that is in string format
class Body(BaseModel):
    text: str

@app.get("/")
def welcome():
    return {"messages":"Welcome to ChatGPT AI Application Version 2"}


@app.post("/generate_response")
def generate_response(body:Body):
    prompt=body.text   #User input to be received in string format
    thread= client.beta.threads.create()
    message = client.beta.threads.messages.create( thread_id=thread.id, role="user",
                                                  content=prompt)
    
    run = client.beta.threads.runs.create(thread_id=thread.id, 
                                          assistant_id=Assistant_key)
    
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run.status=='completed':
            messages=client.beta.threads.messages.list(thread_id=thread.id)
            latest_message= messages.data[0]
            text= latest_message.content[0].text.value
            break;
    return text


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

