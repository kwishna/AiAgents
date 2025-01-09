from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
import dotenv

dotenv.load_dotenv()

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

"""
The CodeAgent is our default agent. It will write and execute python code snippets at each step.

By default, the execution is done in your local environment.
This should be safe because the only functions that can be called are the tools you provided
(especially if it’s only tools by Hugging Face) and a set of predefined safe functions like print or functions from the math module,
so you’re already limited in what can be executed.

The Python interpreter also doesn’t allow imports by default outside of a safe list, so all the most obvious attacks
shouldn’t be an issue. You can authorize additional imports by passing the authorized modules as a list of strings
in argument additional_authorized_imports upon initialization of your CodeAgent:
"""