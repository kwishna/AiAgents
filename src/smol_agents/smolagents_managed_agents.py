from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, ManagedAgent

model = HfApiModel()

web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="web_search",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[managed_web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")