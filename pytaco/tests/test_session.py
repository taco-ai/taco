import os

import pytest
from taco.session import Session, SystemPrompt, UserPrompt
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@pytest.mark.asyncio
async def test_simple_prompty():
    s = Session(SystemPrompt(content="You are an agent named Jeanie. Plesae introduce yourself"))
    response = await s.chat(UserPrompt(content="Hello!"))
    print(response)
