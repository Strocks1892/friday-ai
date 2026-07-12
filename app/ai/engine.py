import os

from dotenv import load_dotenv
from google import genai

from app.prompts.system_prompt import SYSTEM_PROMPT

load_dotenv()


class AIEngine:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate(self, history: str):

        response = self.client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=f"""
{SYSTEM_PROMPT}

Conversation History:

{history}
"""
        )

        return response.text