"""
taco.py - a framework for doing agents/sessions using chatgpt open ai.
"""
import os
import openai
from dotenv import load_dotenv
from taco.session import Session, SystemPrompt, UserPrompt
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
import asyncio

async def main():
    s = Session(system_prompt=SystemPrompt(content="You are a helpful assistant named genie. Introduce yourself"))
    response = await s.chat(UserPrompt(content="hello!"))
    print(response)

if __name__ == '__main__':
    asyncio.run(main())