from smolagents import CodeAgent, DuckDuckGoSearchTool
from smolagents.agents import ToolCallingAgent
from smolagents import tool, TransformersModel, LiteLLMModel
from typing import Optional
import yfinance as yf

model = LiteLLMModel(
    model_id="gpt-4o",
    api_key="Your_API_KEY"
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    additional_authorized_imports=["yfinance"],
    model=model
)
response = agent.run(
"Fetch the stock price of Apple Inc (NASDAQ: AAPL). Use the YFinance Library."
)
print(response)