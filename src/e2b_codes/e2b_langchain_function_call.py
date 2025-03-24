from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.schema import HumanMessage, AIMessage, FunctionMessage
from e2b_code_interpreter import Sandbox

from dotenv import load_dotenv
load_dotenv()

def execute_python(code: str):
    with Sandbox() as sandbox:
        execution = sandbox.run_code(code)
        return execution.text

# Define a tool that uses the E2B Sandbox
e2b_sandbox_tool = Tool(
    name="execute_python",
    func=execute_python,
    description="Execute python code in a Jupyter notebook cell and return result"
)

# Initialize the language model and bind the tool
llm = ChatOpenAI(model="gpt-4o").bind_tools([e2b_sandbox_tool])

# Define the messages
messages = [
    HumanMessage(content="Calculate how many 'r's are in the word 'strawberry'.")
]

# Run the model with a prompt
result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))

# Check if the model called the tool
if result.additional_kwargs.get('tool_calls'):
    tool_call = result.additional_kwargs['tool_calls'][0]
    if tool_call['function']['name'] == "execute_python":
        code = tool_call['function']['arguments']
        execution_result = execute_python(code)

        # Send the result back to the model
        messages.append(
            FunctionMessage(name="execute_python", content=execution_result)
        )

final_result = llm.invoke(messages)
print(final_result.content)
