"""
taco.py - a framework for doing agents/sessions using chatgpt open ai.
"""
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == '__main__':
    print("hello, world!")
