from groq import Groq
import os

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please set it as an environment variable.")

client = Groq(api_key=api_key)


def query_groq(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error querying Groq: {str(e)}"


if __name__ == "__main__":
    print("=== Groq LLaMA Query ===")

    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Groq API...")
    result = query_groq(user_prompt)

    print("\nResponse:")
    print(result)