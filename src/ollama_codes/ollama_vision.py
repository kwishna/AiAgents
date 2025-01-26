# CLI: ollama run llama3.2-vision "describe this architecture: /Users/arch.png"
# CLI: cd Documents && ollama run llama3.2-vision "describe this architecture: "./arch.png"

import ollama

image_path = '/Users/krishna/Downloads/images/high_level_design.png'

# Use Ollama to analyze the image with Llama 3.2-Vision
response = ollama.chat(
    model="llama3.2-vision",
    messages=[{
      "role": "user",
      "content": "You're an experience software architect, you're very good at teaching archtiture to your colleagues."
      "You're given a high level design of Monitoring System on AWS. You should break it down into smaller parts and "
      "Explain it your colleague in such a way that he/she is able to understand it clearly. Also, give real application examples "
      "to ensure he/she could easily relate and understand the entire concept clearly.",
      "images": [image_path]
    }],
)

resp = response['message']['content']
print(f"Response: {resp}")