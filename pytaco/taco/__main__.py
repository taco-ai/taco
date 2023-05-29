"""
taco.py - a framework for doing agents/sessions using chatgpt open ai.
"""
import asyncio
import os

import openai
from dotenv import load_dotenv
import uvicorn

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':
    config = uvicorn.Config("taco.api:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()