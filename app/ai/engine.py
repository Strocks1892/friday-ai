import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.prompts.system_prompt import SYSTEM_PROMPT

from app.tools.weather_function import get_weather

from app.tools.browser_search_function import search_web

from app.tools.function import (
    calculate,
    get_datetime,
    open_application
)

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
""",
            config=types.GenerateContentConfig(
                tools=[
                    calculate,
                    get_datetime,
                    open_application,
                     get_weather,
                     search_web,
                ]
            )
        )

        return response.text