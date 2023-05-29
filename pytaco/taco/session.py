import openai
import os
from typing import Optional, List, Callable, Awaitable
from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"

class Prompt(BaseModel):
    role: Role
    content : str

class AssistantPrompt(Prompt):
    role = Role.assistant

class UserPrompt(Prompt):
    role = Role.user

class SystemPrompt(Prompt):
    role = Role.system

class Session:

    def __init__(self, system_prompt: SystemPrompt, initial_examples: Optional[List[AssistantPrompt]] = None):
        self.messages : List[Prompt] = []
        self.messages.append(system_prompt)
        if initial_examples:
            self.messages.extend(initial_examples)

    async def chat(self, user: UserPrompt) -> Prompt:
        self.messages.append(user)
        completion = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo",
                                                         messages=[m.dict() for m in self.messages])

        return Prompt(**completion.choices[0].message)
    
        