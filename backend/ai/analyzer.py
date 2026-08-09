import json
import requests

from ai.prompts import SYSTEM_PROMPT
from ai.schemas import MessageAnalysis


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


def analyze_message(message: str) -> MessageAnalysis:

    prompt = f"""
{SYSTEM_PROMPT}

Analyze this message:

----------------
{message}
----------------

Return ONLY valid JSON.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "format": MessageAnalysis.model_json_schema(),
            "options": {
                "temperature": 0
            }
        }
    )

    response.raise_for_status()

    data = response.json()

    result = json.loads(data["response"])

    analysis = MessageAnalysis.model_validate(result)

    return analysis
