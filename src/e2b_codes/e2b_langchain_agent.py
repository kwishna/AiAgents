from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from e2b_code_interpreter import Sandbox

from dotenv import load_dotenv
load_dotenv()

system_prompt = "You are a helpful assistant that can execute python code in a Jupyter notebook. Only respond with the code to be executed and nothing else. Strip backticks in code blocks."
prompt = "Calculate how many r's are in the word 'strawberry'"

# Define the tool
@tool
def execute_python(code: str):
    """
    Execute python code in a Jupyter notebook.
    """
    with Sandbox() as sandbox:
        execution = sandbox.run_code(code)
        return execution.text

# Define LangChain components
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [execute_python]
llm = ChatOpenAI(model="gpt-4o", temperature=0)

agent = create_tool_calling_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
agent_executor.invoke({"input": prompt})
