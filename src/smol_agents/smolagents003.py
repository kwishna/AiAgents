"""
We can mention the python libraries that can be used in code. It's like whitelist.

agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['requests', 'bs4'])
"""

from smolagents import CodeAgent, HfApiModel
import dotenv

dotenv.load_dotenv()

agent = CodeAgent(tools=[], model=HfApiModel(), additional_authorized_imports=['requests', 'bs4'])
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")