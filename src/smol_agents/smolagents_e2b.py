from smolagents import CodeAgent, VisitWebpageTool, HfApiModel
agent = CodeAgent(
    tools = [VisitWebpageTool()],
    model=HfApiModel(),
    additional_authorized_imports=["requests", "markdownify"],
    use_e2b_executor=True
)
agent.run("Who was the 1st person landing on the Moon?")

"""
What is E2B?

E2B is an open-source infrastructure that allows you run to AI-generated code in secure isolated sandboxes in the cloud.
To start and control sandboxes, use our Python SDK or JavaScript SDK.
"""