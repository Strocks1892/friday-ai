import os

from dotenv import load_dotenv
from google import genai

from app.models.chat import ChatResponse

from app.prompts.system_prompt import SYSTEM_PROMPT

from app.utils.logger import logger

from app.core.memory import conversation_history

from app.tools.function import (
    calculate,
    get_datetime,
    open_application
)

load_dotenv()

class ChatService:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.tool_manager = ToolManager()
        
    def get_response(self, message: str) -> ChatResponse:
        try:
            logger.info("Generating response from gemini...")

            # -------------------------------
            # Check if any tool can handle it
            # -------------------------------
            tool_response = self.tool_manager.execute(message)

            if tool_response:
                return ChatResponse(
                    response=tool_response
                )

            # -------------------------------
            # Store user message
            # -------------------------------
            conversation_history.append({
                "role": "user",
                "text": message
            })

            # -------------------------------
            # Build conversation history
            # -------------------------------
            
            history = ""

            for msg in conversation_history:
                history += f"{msg['role']}: {msg['text']}\n"

            # -------------------------------
            # Ask Gemini
            # -------------------------------
            response = self.client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=f"""
                {SYSTEM_PROMPT}

                Conversation history:
                {history}
                """,
            )

            # -------------------------------
            # Save AI response
            # -------------------------------
            
            conversation_history.append({
                "role": "assistant",
                "text": response.text
            })

            logger.info("Response generated successfully.")

            return ChatResponse(
                response=response.text
            )

        except Exception as e:
            logger.error(f"Gemini Error: {e}")

            return ChatResponse(
                response="Sorry, I'm unable to process your request right now. Please try again in a few moments."
            )