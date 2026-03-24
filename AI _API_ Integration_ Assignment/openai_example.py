from openai import OpenAI
import os

# Get API key from environment variable
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found. Please set it as an environment variable.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def query_openai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="google/gemma-3-4b-it:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("=== OpenAI (via OpenRouter) Query ===")

    user_prompt = input("Enter your prompt: ").strip()

    if not user_prompt:
        print("Prompt cannot be empty.")
    else:
        print("\nQuerying OpenAI (via OpenRouter)...")
        result = query_openai(user_prompt)

        print("\nResponse:")
        print(result)