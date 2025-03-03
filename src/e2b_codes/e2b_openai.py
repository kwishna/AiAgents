from dotenv import load_dotenv
from openai import OpenAI
from e2b_code_interpreter import Sandbox


load_dotenv()

client = OpenAI()
system = "You are a helpful assistant that can execute python code in a Jupyter notebook. Only respond with the code to be executed and nothing else. Strip backticks in code blocks."
prompt = "Calculate how many r's are in the word 'strawberry'"

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
)

code = response.choices[0].message.content

if code:
    with Sandbox() as sandbox:
        execution = sandbox.run_code(code)
        result = execution.text
    print(result)
