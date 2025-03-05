from openai import OpenAI
from e2b_code_interpreter import Sandbox
import json

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
model = "gpt-4o"

messages = [
    {
        "role": "user",
        "content": "Calculate how many r's are in the word 'strawberry'"
    }
]


tools = [{
    "type": "function",
    "function": {
        "name": "execute_python",
        "description": "Execute python code in a Jupyter notebook cell and return result",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The python code to execute in a single cell"
                }
            },
            "required": ["code"]
        }
    }
}]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
)

response_message = response.choices[0].message
messages.append(response_message)

if response_message.tool_calls:
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "execute_python":
            # Create a sandbox and execute the code
            with Sandbox() as sandbox:
                code = json.loads(tool_call.function.arguments)['code']
                execution = sandbox.run_code(code)
                result = execution.text

            # Send the result back to the model
            messages.append({
                "role": "tool",
                "name": "execute_python",
                "content": result,
                "tool_call_id": tool_call.id,
            })

final_response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(final_response.choices[0].message.content)