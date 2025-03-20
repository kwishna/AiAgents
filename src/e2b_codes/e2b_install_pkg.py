from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv
load_dotenv()

sbx = Sandbox()
sbx.commands.run("pip install cowsay") # This will install the cowsay package
sbx.run_code("""
  import cowsay
  cowsay.cow("Hello, world!")
""")


# npm packages
sbx.commands.run("npm install cowsay") # This will install the cowsay package
sbx.run_code("""
  import { say } from 'cowsay'
  console.log(say('Hello, world!'))
""", language="javascript")
