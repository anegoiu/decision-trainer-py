
import os
import sys
import warnings
from dotenv import load_dotenv

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Suppress all warnings
try:
    from decision_trainer.suppress_warnings import suppress_all_warnings
except ImportError:
    # Fallback if module not found
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", message=".*PydanticDeprecatedSince.*")
    warnings.filterwarnings("ignore", message=".*deprecated.*")

# Load environment variables from .env file
load_dotenv()

# Set environment variable BEFORE importing weave to disable CrewAI tracing
os.environ["WEAVE_TRACE_CREWAI"] = "false"

import weave
import json
from openai import OpenAI


@weave.op() # 🐝 Decorator to track requests
def extract_fruit(sentence: str) -> dict:
    client = OpenAI()  # Will automatically use OPENAI_API_KEY from environment
    system_prompt = "Parse sentences into a JSON dict with keys: fruit, color and flavor."
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": sentence}
      ],
      temperature=0.7,
      response_format={"type": "json_object"}
    )
    extracted = response.choices[0].message.content
    print("example output: ", extracted)
    return json.loads(extracted)


# Initialize weave
weave.init('decision_trainer') # 🐝
sentence = "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy."
extract_fruit(sentence)