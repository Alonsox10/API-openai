from openai import AsyncOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import os


load_dotenv()

client = AsyncOpenAI(api_key= os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class ResponsePrompt(BaseModel):
    prompt: str


@app.post("/message")
async def returnMessage(data: ResponsePrompt):
    response = await client.chat.completions.create(
        model="gpt-5.2",
        messages=[{"role":"user" , "content": data.prompt}]

    )

    return {
        "message": response.choices[0].message.content
    }