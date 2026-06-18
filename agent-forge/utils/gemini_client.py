import os
import google.generativeai as genai
from dotenv import load_dotenv
import time
load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_gemini(prompt):

    for attempt in range(3):

        try:

            response = model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:

            print(
                f"Retry {attempt+1}"
            )

            time.sleep(5)

    raise Exception(
        "Gemini failed after retries"
    )