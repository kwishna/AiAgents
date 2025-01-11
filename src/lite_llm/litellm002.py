from litellm import completion
import os
import dotenv

dotenv.load_dotenv()

response = completion(
  model="openai/gpt-4o",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)

for chunk in response:
    print("--- chunk ----")
    print(chunk.choices[0].delta.content)