FROM e2bdev/code-interpreter:latest

RUN pip install cowsay
RUN npm install cowsay

# e2b template build -c "/root/.jupyter/start-up.sh"
# from e2b_code_interpreter import Sandbox
# sbx = Sandbox(template='YOUR_TEMPLATE_ID')

