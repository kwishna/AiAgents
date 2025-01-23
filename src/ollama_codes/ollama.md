## Understanding Ollama Commands
### Ollama uses simple commands to manage models. Here are some key commands you'll need:

```
ollama -v: Checks the installed version of Ollama.
ollama pull <model_name>:<tag>: Downloads a model from the Ollama library.
ollama run <model_name>:<tag>: Runs a model and starts an interactive chat session.
ollama create <model_name> -f <Modelfile>: Creates a custom model using a Modelfile.
ollama show <model_name>: Shows information about a model.
ollama ps: Lists the models that are currently running.
ollama stop <model_name>: Unloads a model from memory.
ollama cp <source_model> <destination_model>: Copies a model.
ollama delete <model_name>: Deletes a model.
ollama push <model_name>:<tag>: Uploads a model to a model library.
```

# Ollama Python Library

The Ollama Python library provides the easiest way to integrate Python 3.8+ projects with [Ollama](https://github.com/ollama/ollama).

## Prerequisites

- [Ollama](https://ollama.com/download) should be installed and running
- Pull a model to use with the library: `ollama pull <model>` e.g. `ollama pull llama3.2`
  - See [Ollama.com](https://ollama.com/search) for more information on the models available.

## Install

```sh
pip install ollama
```

## Usage

```python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
```

See [_types.py](ollama/_types.py) for more information on the response types.

## Streaming responses

Response streaming can be enabled by setting `stream=True`.

```python
from ollama import chat

stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```

## Custom client
A custom client can be created by instantiating `Client` or `AsyncClient` from `ollama`.

All extra keyword arguments are passed into the [`httpx.Client`](https://www.python-httpx.org/api/#client).

```python
from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
```

## Async client

The `AsyncClient` class is used to make asynchronous requests. It can be configured with the same fields as the `Client` class.

```python
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='llama3.2', messages=[message])

asyncio.run(chat())
```

Setting `stream=True` modifies functions to return a Python asynchronous generator:

```python
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient().chat(model='llama3.2', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())
```

## API

The Ollama Python library's API is designed around the [Ollama REST API](https://github.com/ollama/ollama/blob/main/docs/api.md)

### Chat

```python
ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
```

### Generate

```python
ollama.generate(model='llama3.2', prompt='Why is the sky blue?')
```

### List

```python
ollama.list()
```

### Show

```python
ollama.show('llama3.2')
```

### Create

```python
ollama.create(model='example', from_='llama3.2', system="You are Mario from Super Mario Bros.")
```

### Copy

```python
ollama.copy('llama3.2', 'user/llama3.2')
```

### Delete

```python
ollama.delete('llama3.2')
```

### Pull

```python
ollama.pull('llama3.2')
```

### Push

```python
ollama.push('user/llama3.2')
```

### Embed

```python
ollama.embed(model='llama3.2', input='The sky is blue because of rayleigh scattering')
```

### Embed (batch)

```python
ollama.embed(model='llama3.2', input=['The sky is blue because of rayleigh scattering', 'Grass is green because of chlorophyll'])
```

### Ps

```python
ollama.ps()
```


## Errors

Errors are raised if requests return an error status or if an error is detected while streaming.

```python
model = 'does-not-yet-exist'

try:
  ollama.chat(model)
except ollama.ResponseError as e:
  print('Error:', e.error)
  if e.status_code == 404:
    ollama.pull(model)
```

## cURL

### Prompt
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:7b",
  "prompt": "Write a short poem about the stars."
}'
```

### Chat Completion
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1:7b",
  "messages": [
    {
      "role": "user",
      "content": "Write a short poem about the stars."
    }
  ]
}'
```

### Supported Endpoints and Features
#### Here's a breakdown of the supported endpoints and their features:
```
/v1/chat/completions

- Purpose: Generate chat-style responses.
- Supported Features:
    Chat completions (multi-turn conversations).
    Streaming responses (real-time output).
    JSON mode (structured JSON output).
    Reproducible outputs (using a seed).
    Vision (multimodal models like llava that can process images).
    Tools (function calling).

- Supported Request Fields:
    model: The name of the Ollama model to use.
    messages: An array of message objects, each with a role (system user, assistant, or tool) and content (text or image).
    frequency_penalty, presence_penalty: Controls repetition.
    response_format: Specifies the output format (e.g. json).
    seed: For reproducible outputs.
    stop: Sequences to stop generation.
    stream: Enables/disables streaming.
    stream_options: Additional options for streaming.
    include_usage: Includes usage information in the stream.
    temperature: Controls randomness.
    top_p: Controls diversity.
    max_tokens: Maximum tokens to generate.
    tools: List of tools the model can access.
```

```
/v1/completions

- Purpose: Generate text completions.
- Supported Features:
    Text completions (single-turn generation).
    Streaming responses.
    JSON mode
    Reproducible outputs.

- Supported Request Fields:
    model: The name of the Ollama model.
    prompt: The input text.
    frequency_penalty, presence_penalty: Controls repetition.
    seed: For reproducible outputs.
    stop: Stop sequences.
    stream: Enables/disables streaming.
    stream_options: Additional options for streaming.
    include_usage: Includes usage information in the stream.
    temperature: Controls randomness.
    top_p: Controls diversity.
    max_tokens: Maximum tokens to generate.
    suffix: Text to append after the model's response
```

```
/v1/models
```

```
/v1/models/{model}
```

```
/v1/embeddings
```

## How to Use Ollama with OpenAI Clients
OpenAI Python Library:
```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # Required but ignored
)

# Example chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'user', 'content': 'Say this is a test'},
    ],
    model='deepseek-r1:7b',
)

# Example text completion
completion = client.completions.create(
    model="deepseek-r1:7b",
    prompt="Say this is a test",
)

# Example list models
list_completion = client.models.list()

# Example get model info
model = client.models.retrieve("deepseek-r1:7b")
```

## OpenAI JavaScript Library:
```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'http://localhost:11434/v1/',
  apiKey: 'ollama', // Required but ignored
});

// Example chat completion
const chatCompletion = await openai.chat.completions.create({
  messages: [{ role: 'user', content: 'Say this is a test' }],
  model: 'deepseek-r1:7b',
});

// Example text completion
const completion = await openai.completions.create({
  model: "deepseek-r1:7b",
  prompt: "Say this is a test.",
});

// Example list models
const listCompletion = await openai.models.list()

// Example get model info
const model = await openai.models.retrieve("deepseek-r1:7b")
```

## curl (Direct API Calls):
Chat completion
```bash
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseek-r1:7b",
        "messages": [
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```
```bash
# Text completion
curl http://localhost:11434/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseek-r1:7b",
        "prompt": "Say this is a test"
    }'
```
```bash
# List models
curl http://localhost:11434/v1/models
```
```bash
# Get model info
curl http://localhost:11434/v1/models/deepseek-r1:7b
```
```bash
# Embeddings
curl http://localhost:11434/v1/embeddings \
    -H "Content-Type: application/json" \
    -d '{
        "model": "all-minilm",
        "input": ["why is the sky blue?", "why is the grass green?"]
    }'
```