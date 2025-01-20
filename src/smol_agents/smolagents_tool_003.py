from huggingface_hub import list_models
from smolagents import Tool, CodeAgent, HfApiModel
import dotenv

dotenv.load_dotenv()

class ModelDownloadTool(Tool):
    name = "model_download_tool"
    description = "This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub. It returns the name of the checkpoint."
    inputs = {"task": {"type": "string", "description": "The task for which to get the download count."}}
    output_type = "string"

    def forward(self, task: str = "text-classification") -> str:
        most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return most_downloaded_model.id

agent = CodeAgent(tools=[ModelDownloadTool()], model=HfApiModel())
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)

"""
The subclass needs the following attributes:

    A clear name. The name should be descriptive enough of what this tool does to help the LLM brain powering the agent.
    Since this tool returns the model with the most downloads for a task, let’s name it model_download_tool.
    
    A description. Same as for the name, this description is an instruction manual for the LLM powering you agent,
    so do not neglect it. Input types and descriptions
    
    Output type All these attributes will be automatically baked into the agent’s system prompt upon initialization:
    so strive to make them as clear as possible!


"""