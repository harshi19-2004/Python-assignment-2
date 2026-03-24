import cohere
import os

# Get API key ONLY from environment variable (no default value)
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    raise ValueError("COHERE_API_KEY not found. Please set it as an environment variable.")

co = cohere.Client(api_key)


def query_cohere(prompt: str) -> str:
    try:
        response = co.chat(
            model="command-r7b-12-2024",
            message=prompt,
            temperature=0.7,
        )
        return response.text.strip()

    except Exception as e:
        return f"Error querying Cohere: {str(e)}"


if __name__ == "__main__":
    print("=== Cohere Query ===")
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Cohere API...")
    result = query_cohere(user_prompt)
    print("\nResponse:")
    print(result)