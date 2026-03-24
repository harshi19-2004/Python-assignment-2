import requests

# Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MODEL = "tinyllama"


def query_ollama(prompt: str, model: str = DEFAULT_MODEL) -> str:
    try:
        url = f"{OLLAMA_BASE_URL}/api/generate"

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 200,
            },
        }

        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()

        data = response.json()
        return data.get("response", "No response received.").strip()

    except requests.exceptions.ConnectionError:
        return "Error: Ollama not running. Use: ollama serve"
    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except Exception as e:
        return f"Error querying Ollama: {str(e)}"


if __name__ == "__main__":
    print("=== Ollama Local Model Query ===")
    print(f"Model: {DEFAULT_MODEL}")

    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
    else:
        print("\nQuerying Ollama...")
        result = query_ollama(prompt)

        print("\nResponse:")
        print(result)