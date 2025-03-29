# Use Ubuntu as the base image
# Note: Use `FROM e2bdev/code-interpreter:latest` instead if you want to use the code interpreting features (https://github.com/e2b-dev/code-interpreter)
# and not just plain E2B sandbox.
FROM ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable Docker repository
RUN echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
RUN apt-get update && apt-get install -y docker-ce=5:27.1.1-1~ubuntu.20.04~focal docker-ce-cli=5:27.1.1-1~ubuntu.20.04~focal containerd.io

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the default command
CMD ["/bin/bash"]



# Run npm i -g @e2b/cli@latest to install the latest version of the E2B CLI.
# Run e2b template init in your project directory.
# Copy the e2b.Dockerfile into your project.
# Run e2b template build to build your sandbox.
# Start the sandbox either via our SDK or the E2B CLI like this e2b sandbox spawn <sandbox-template-id>.

# from e2b import Sandbox
# sbx = Sandbox.create('e2b-with-docker')
# result = sbx.commands.run('docker --version')
# print(result.stdout)
# sbx.kill()