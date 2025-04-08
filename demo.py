import os

from groq import Groq
from dotenv import load_dotenv
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "hi",
        }
    ],
    model="mistral-saba-24b",
)

print(chat_completion.choices[0].message.content)