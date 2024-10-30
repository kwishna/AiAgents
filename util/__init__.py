# from pathlib import Path
# load_dotenv(dotenv_path=Path('.env').resolve())

import os
from dotenv import load_dotenv
load_dotenv()

def get_openai_api_key():
    return os.environ['OPENAI_API_KEY']
