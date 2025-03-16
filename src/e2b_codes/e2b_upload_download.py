from e2b_code_interpreter import Sandbox

sbx = Sandbox()

# ---------- upload ---------
# Read local file relative to the current working directory
with open("local/file", "rb") as file:
   # Upload file to the sandbox to absolute path '/home/user/my-file'
	sbx.files.write("/home/user/my-file", file)

# ---------- download ---------
# Download file from the sandbox to absolute path '/home/user/my-file'
content = sbx.files.read('/home/user/my-file')
# Write file to local path relative to the current working directory
with open('local/file', 'w') as file:
    file.write(content)
