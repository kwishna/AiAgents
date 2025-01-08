import dotenv
from litellm import completion

dotenv.load_dotenv()

# response = completion(
#             model="ollama/llama2",
#             messages = [{ "content": "Hello, how are you?","role": "user"}],
#             api_base="http://localhost:11434"
# )
# print(response)

## set ENV variables

response = completion(model="openai/gpt-4o", messages=[{"content": "Hello, how are you?", "role": "user"}])

print(response.choices[0].message.content)
