import os

from dotenv import load_dotenv
from google import genai

from app.models.chat import ChatResponse

load_dotenv()


class ChatService:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def get_response(self, message: str) -> ChatResponse:
        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=message,
        )

        return ChatResponse(
            response=response.text
        )
        print(response)