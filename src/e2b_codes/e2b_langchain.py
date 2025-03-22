from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from e2b_code_interpreter import Sandbox

from dotenv import load_dotenv
load_dotenv()

system_prompt = "You are a helpful assistant that can execute python code in a Jupyter notebook. Only respond with the code to be executed and nothing else. Strip backticks in code blocks."
prompt = "Calculate how many r's are in the word 'strawberry'"

# Create LangChain components
llm = ChatOpenAI(model="gpt-4o")
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

output_parser = StrOutputParser()

# Create the chain
chain = prompt_template | llm | output_parser

# Run the chain
code = chain.invoke({"input": prompt})

# Execute code in E2B Sandbox
with Sandbox() as sandbox:
    execution = sandbox.run_code(code)
    result = execution.text

print(result)
