from smolagents import ToolCallingAgent, HfApiModel
import dotenv

dotenv.load_dotenv()

"""
We also support the widely-used way of writing actions as JSON-like blobs: this is ToolCallingAgent,
it works much in the same way like CodeAgent, of course without additional_authorized_imports since it doesn’t execute code.
"""

agent = ToolCallingAgent(tools=[], model=HfApiModel())
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")