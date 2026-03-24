"""
multi_api_query.py
Unified program to query multiple AI providers
"""

import os
import requests
from openai import OpenAI
from groq import Groq
from huggingface_hub import InferenceClient
import cohere

# ══════════════════════════════════════════════════════
#  API KEYS (Environment Variables ONLY)
# ══════════════════════════════════════════════════════
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")


# ══════════════════════════════════════════════════════
#  1. OpenAI (via OpenRouter)
# ══════════════════════════════════════════════════════
def query_openai(prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        return "Error: OPENROUTER_API_KEY not set"

    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )

        response = client.chat.completions.create(
            model="google/gemma-3-4b-it:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error (OpenAI/OpenRouter): {e}"


# ══════════════════════════════════════════════════════
#  2. Groq
# ══════════════════════════════════════════════════════
def query_groq(prompt: str) -> str:
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY not set"

    try:
        client = Groq(api_key=GROQ_API_KEY)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error (Groq): {e}"


# ══════════════════════════════════════════════════════
#  3. Ollama (Local)
# ══════════════════════════════════════════════════════
def query_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()
        return response.json().get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return "Error: Ollama not running (use: ollama serve)"
    except Exception as e:
        return f"Error (Ollama): {e}"


# ══════════════════════════════════════════════════════
#  4. Hugging Face
# ══════════════════════════════════════════════════════
def query_huggingface(prompt: str) -> str:
    if not HF_API_KEY:
        return "Error: HUGGINGFACE_API_KEY not set"

    try:
        client = InferenceClient(
            provider="auto",
            api_key=HF_API_KEY,
        )

        response = client.chat_completion(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error (Hugging Face): {e}"


# ══════════════════════════════════════════════════════
#  5. Cohere
# ══════════════════════════════════════════════════════
def query_cohere(prompt: str) -> str:
    if not COHERE_API_KEY:
        return "Error: COHERE_API_KEY not set"

    try:
        co = cohere.Client(COHERE_API_KEY)

        response = co.chat(
            model="command-r7b-12-2024",
            message=prompt,
            temperature=0.7,
        )

        return response.text.strip()

    except Exception as e:
        return f"Error (Cohere): {e}"


# ══════════════════════════════════════════════════════
#  MENU
# ══════════════════════════════════════════════════════
PROVIDERS = {
    "1": ("OpenRouter (Gemma)", query_openai),
    "2": ("Groq (LLaMA 3.1)", query_groq),
    "3": ("Ollama (Local)", query_ollama),
    "4": ("Hugging Face", query_huggingface),
    "5": ("Cohere", query_cohere),
}


def print_menu():
    print("\n" + "=" * 45)
    print("        MULTI-API AI QUERY TOOL")
    print("=" * 45)
    for key, (name, _) in PROVIDERS.items():
        print(f"  [{key}] {name}")
    print("  [q] Quit")
    print("=" * 45)


def main():
    print("\nWelcome to Multi-API Query Tool!")

    while True:
        print_menu()
        choice = input("Select provider (1-5) or q: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in PROVIDERS:
            print("Invalid choice.")
            continue

        provider_name, query_fn = PROVIDERS[choice]
        prompt = input("\nEnter your prompt: ").strip()

        if not prompt:
            print("Prompt cannot be empty.")
            continue

        print(f"\nQuerying {provider_name}...")
        result = query_fn(prompt)

        print(f"\n--- {provider_name} Response ---")
        print(result)
        print("-" * 45)


if __name__ == "__main__":
    main()