import os
from smolagents import CodeAgent, HfApiModel
import dotenv

dotenv.load_dotenv()

model_id = "meta-llama/Llama-3.3-70B-Instruct"

# model = HfApiModel(model_id=model_id, token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")    # Huggingface model
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct"")       # Using local 'transformer' model
# model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key="YOUR_ANTHROPIC_API_KEY") # Using LiteLLM (OpenAI or Anthropic. Environment variable ANTHROPIC_API_KEY or OPENAI_API_KEY, or pass api_key

model = HfApiModel(model_id=model_id, token=os.environ["HF_ACCESS_TOKEN"])
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

"""
===================
Ollama
===================

from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/llama3.2", # This model is a bit weak for agentic behaviours though
    api_base="http://localhost:11434", # replace with remote open-ai compatible server if necessary
    api_key="YOUR_API_KEY" # replace with API key if necessary
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
"""