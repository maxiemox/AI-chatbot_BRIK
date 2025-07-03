# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyB5u8_y1cIzvNtyWIP2VoFK5P3xHjaAR-w"
    )

    model = "gemini-2.5-pro"
    history = []

    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Be a friendly ,warm and clear chatbot designed to help students with code, tech career doubts .Respond in 2-4 sentences ,reply unless user requests for  detailed explanations. Use calm, encouraging tone. """),
        ],
    )
    while True:
        question = input("\n you: ")
        if question.lower() in ['exit','quit']:
            print("chatbot: conversation ended! see you next time,  Have a great day!")
            break
        contents = history + [
            types.Content(
            role = "user",
            parts = [
 types.Part.from_text(text = question),
            ],
         )
        ]
        response_text = ""    
        for chunk in client.models.generate_content_stream(
          model=model,
          contents=contents,
          config=generate_content_config,
    ):
          response_text += chunk.text
        
         
        print(f"\nChatbot:{response_text.strip()}")
        
        print(f"📊 Tokens used in this round: {chunk.usage_metadata.total_token_count}")

        history.append(types.Content(
            role = "user",
            parts = [types.Part.from_text(text=question)],
        ))
        history.append(types.Content(
            role = "model",
            parts = [types.Part.from_text(text = response_text)],
        ))

if __name__ == "__main__":
    generate()
