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
    try:

        response = await client.responses.create(
            model="gpt-5-mini",
            input=[
                {
                    "role":"user",
                    "content": [
                        {
                            "type":"input_text",
                            "text": data.prompt
                        }
                    ]
                }
            ]
        )

        message = response.output_text
        return message
    except Exception as e:
        return {"error": str(e)}