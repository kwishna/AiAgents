from smolagents import load_tool

search_tool = load_tool("web_search")
print(search_tool("Who's the current president of Russia?"))

"""
A tool is an atomic function to be used by an agent. To be used by an LLM, it also needs a few attributes that constitute its API and will be used to describe to the LLM how to call this tool:

   A name
   A description
   Input types and descriptions
   An output type

You can for instance check the PythonInterpreterTool: it has a name, a description, input descriptions, an output type, and a forward method to perform the action.

When the agent is initialized, the tool attributes are used to generate a tool description which is baked into the agent’s system prompt. This lets the agent know which tools it can use and why.
Default toolbox

Transformers comes with a default toolbox for empowering agents, that you can add to your agent upon initialization with argument add_base_tools = True:

   DuckDuckGo web search*: performs a web search using DuckDuckGo browser.
   Python code interpreter: runs your the LLM generated Python code in a secure environment. This tool will only be added to ToolCallingAgent if you initialize it with add_base_tools=True, since code-based agent can already natively execute Python code
   Transcriber: a speech-to-text pipeline built on Whisper-Turbo that transcribes an audio to text.

You can manually use a tool by calling the load_tool() function and a task to perform.
"""