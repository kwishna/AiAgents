# pip install crewai e2b-code-interpreter
from crewai.tools import tool
from crewai import Agent, Task, Crew, LLM
from e2b_code_interpreter import Sandbox

from dotenv import load_dotenv
load_dotenv()

# Update tool definition using the decorator
@tool("Python Interpreter")  
def execute_python(code: str) -> str:
    """
    Execute Python code and return the results.
    """
    with Sandbox() as sandbox:
        execution = sandbox.run_code(code)
        return execution.text

# Define the agent
python_executor = Agent(
    role='Python Executor',
    goal='Execute Python code and return the results',
    backstory='You are an expert Python programmer capable of executing code and returning results.',
    tools=[execute_python],
    llm=LLM(model="gpt-4o")
)

# Define the task
execute_task = Task(
    description="Calculate how many r's are in the word 'strawberry'",
    agent=python_executor,
    expected_output="The number of r's in the word 'strawberry'"
)

# Create the crew
code_execution_crew = Crew(
    agents=[python_executor],
    tasks=[execute_task],
    verbose=True,
)

# Run the crew
result = code_execution_crew.kickoff()
print(result)
