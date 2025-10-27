# app/api_client.py

import os
from groq import Groq
from dotenv import load_dotenv
from logger import CustomLogger  # Import your custom logger

# ✅ Ensure environment variables from .env are loaded
load_dotenv()

class GroqClient:
    """Class to interact with the Groq API."""

    def __init__(self):
        # ✅ Use the correct environment variable name
        self.api_key = os.getenv('GROQ_API_KEY')

        if not self.api_key:
            raise ValueError("❌ GROQ_API_KEY not found. Please check your .env file.")

        # Initialize Groq client with the loaded API key
        self.client = Groq(api_key=self.api_key)
        self.logger = CustomLogger().get_logger()  # Initialize your custom logger

    def get_response(self, messages):
        """
        Send messages to the Groq API and return the response.

        :param messages: List of messages for the conversation.
        :return: AI response as a string.
        """
        try:
            self.logger.info("Sending messages to Groq API...")
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model="llama-3.1-8b-instant"  # Use the appropriate model
            )
            response = chat_completion.choices[0].message.content
            self.logger.info("Received response from Groq API.")
            return response
        except Exception as e:
            self.logger.error(f"Error communicating with Groq API: {e}")
            return "Sorry, I couldn't get a response at this time."
