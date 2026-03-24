import os
from huggingface_hub import InferenceClient

# Get API key ONLY from environment variable (no default value)
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY not found. Please set it as an environment variable.")

MODEL = "deepseek-ai/DeepSeek-V3-0324"

client = InferenceClient(
    provider="auto",
    api_key=api_key,
)

def query_huggingface(prompt: str) -> str:
    try:
        response = client.chat_completion(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error querying Hugging Face: {str(e)}"


if __name__ == "__main__":
    print("=== Hugging Face Inference API Query ===")
    print(f"Model  : {MODEL}")
    
    user_prompt = input("\nEnter your prompt: ")
    
    print("\nQuerying Hugging Face...")
    result = query_huggingface(user_prompt)

    print("\nResponse:")
    print(result)