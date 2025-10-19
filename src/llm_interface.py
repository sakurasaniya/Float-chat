import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

class LocalLLM:
    def __init__(self):
        # Construct the Hugging Face inference API URL automatically
        self.url = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

    def ask(self, query: str) -> str:
        payload = {
            "inputs": query
        }
        try:
            response = requests.post(self.url, headers=HEADERS, json=payload)
            response.raise_for_status()
            output = response.json()

            if isinstance(output, dict) and "error" in output:
                return f"Error: {output['error']}"

            if isinstance(output, list) and len(output) > 0:
                if isinstance(output[0], str):
                    return output[0]
                elif "generated_text" in output[0]:
                    return output[0]["generated_text"]

            return str(output)
        except Exception as e:
            return f"LLM request failed: {str(e)}"
