# AI API Integration Assignment

**Course:** Generative AI  
**Institution:** CampusPe | Tattva Code Labs  
**Mentor:** Jacob Dennis  
**Year:** 2026

---

## Project Description

This project demonstrates real-world integration with **5 different Generative AI APIs** using Python. Each program accepts a user prompt and returns an AI-generated response from a different provider. A bonus unified tool (`multi_api_query.py`) allows querying all providers from a single interactive menu.

### Providers Integrated:
| # | Provider | Model Used | Type |
|---|---|---|---|
| 1 | OpenAI (via OpenRouter) | google/gemma-3-4b-it:free | Cloud API (Free) |
| 2 | Groq | llama-3.1-8b-instant | Cloud API (Free) |
| 3 | Ollama | tinyllama | Local (Offline) |
| 4 | Hugging Face | deepseek-ai/DeepSeek-V3-0324 | Cloud API (Free) |
| 5 | Cohere | command-r7b-12-2024 | Cloud API (Free) |

---

## Project Structure

```
AI API Integration Assignment/
├── openai_example.py           # Query OpenAI-compatible model via OpenRouter
├── groq_example.py             # Query Groq LLaMA 3.1 model
├── ollama_example.py           # Query local Ollama TinyLlama model
├── huggingface_example.py      # Query Hugging Face DeepSeek model
├── cohere_example.py           # Query Cohere Command-R7B model
├── multi_api_query.py          # Unified multi-provider interactive tool (Bonus)
├── requirements.txt            # All Python dependencies
├── README.md                   # Project documentation
└── screenshots/
    ├── openai_output.png           # OpenAI working output
    ├── groq_output.png             # Groq working output
    ├── ollama_output.png           # Ollama working output
    ├── huggingface_output.png      # Hugging Face working output
    ├── cohere_output.png           # Cohere working output
    ├── multi_api_query_output.png  # Multi-API tool - OpenAI query
    ├── multi_api_query_output2.png # Multi-API tool - Groq query
    ├── multi_api_query_output3.png # Multi-API tool - Ollama query
    ├── multi_api_query_output4.png # Multi-API tool - HuggingFace query
    ├── multi_api_query_output5.png # Multi-API tool - Cohere query
    ├── multi_api_query_output6.png # Multi-API tool - Exit
    ├── Ollama_Installination.png   # Ollama installation proof
    └── Ollama_Windows_PowerShell_Installination.png  # ollama pull tinyllama
```

---

## Setup Instructions

### Step 1 — Clone the Repository
```bash
git clone <your-repository-url>
cd "AI API Integration Assignment"
```

### Step 2 — Install Required Packages
```bash
pip install openai groq requests google-generativeai cohere huggingface_hub
```
Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Step 3 — Set Up API Keys

Use environment variables to keep your keys secure:

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your-groq-key"
$env:HUGGINGFACE_API_KEY="your-hf-token"
$env:COHERE_API_KEY="your-cohere-key"
```

**Linux/Mac:**
```bash
export GROQ_API_KEY="your-groq-key"
export HUGGINGFACE_API_KEY="your-hf-token"
export COHERE_API_KEY="your-cohere-key"
```

### Step 4 — Ollama Local Setup (for ollama_example.py only)
```bash
# Download Ollama from https://ollama.ai/
# Then pull the model
ollama pull tinyllama
# Ollama server starts automatically
```

---

## How to Obtain Each API Key

| Provider | URL | Steps |
|---|---|---|
| **OpenAI (OpenRouter)** | [openrouter.ai](https://openrouter.ai) | Sign up → Keys → Create New Key → Free credits included |
| **Groq** | [console.groq.com](https://console.groq.com) | Sign up → API Keys → Create API Key → Free |
| **Ollama** | [ollama.ai](https://ollama.ai) | Download & install → No API key needed → Runs locally |
| **Hugging Face** | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Sign up → New Token → Read access → Free |
| **Cohere** | [dashboard.cohere.com](https://dashboard.cohere.com) | Sign up → API Keys → New Trial Key → Free tier |

---

## How to Run Each Program

### 1. OpenAI (via OpenRouter)
```bash
python openai_example.py
```
- Uses **OpenRouter** as a free OpenAI-compatible gateway
- Model: `google/gemma-3-4b-it:free`
- No billing required

**Sample Output:**
```
Enter your prompt: what is computer Networks?
Querying OpenAI (via OpenRouter)...

Response:
A computer network is a collection of computers and devices connected
together to share resources and communicate with each other...
```

---

### 2. Groq
```bash
python groq_example.py
```
- Uses Groq's ultra-fast inference engine
- Model: `llama-3.1-8b-instant`
- Free tier available

**Sample Output:**
```
=== Groq LLaMA Query ===
Enter your prompt: what is Ai?

Querying Groq API...

Response:
AI, or Artificial Intelligence, refers to the simulation of human
intelligence in machines that are programmed to think and learn...
```

---

### 3. Ollama (Local — No Internet Required)
```bash
python ollama_example.py
```
- Runs **100% locally** on your machine
- Model: `tinyllama` (637 MB — downloaded once)
- No API key or internet needed after setup

**Sample Output:**
```
=== Ollama Local Model Query ===
Using model: tinyllama | Server: http://localhost:11434
Enter your prompt: what is Deep learning give an example?

Querying Ollama...

Response:
Deep learning, also known as deep neural networks (DNNs), is a type
of artificial neural network that can learn complex relationships...
```

---

### 4. Hugging Face
```bash
python huggingface_example.py
```
- Uses `InferenceClient` with `provider="auto"` 
- Model: `deepseek-ai/DeepSeek-V3-0324`
- Automatically routes to best available free provider

**Sample Output:**
```
=== Hugging Face Inference API Query ===
Model  : deepseek-ai/DeepSeek-V3-0324

Enter your prompt: what is IT?

Querying Hugging Face...

Response:
IT (Information Technology) refers to the use of computers, networks,
software, and other digital systems to store, process, transmit...
```

---

### 5. Cohere
```bash
python cohere_example.py
```
- Uses Cohere's Chat API (`co.chat()`)
- Model: `command-r7b-12-2024`
- Note: The old Generate API was deprecated in September 2025

**Sample Output:**
```
=== Cohere Query ===
Enter your prompt: what is Machine Learning?

Querying Cohere API...

Response:
Machine learning (ML) is a branch of computer science that focuses on
developing algorithms and models that enable computers to learn and
make predictions or decisions without being explicitly programmed...
```

---

### 6. Multi-API Tool — Bonus ⭐
```bash
python multi_api_query.py
```
Unified interactive menu to query any of the 5 providers:

```
Welcome to Multi-API Query Tool!

=============================================
        MULTI-API AI QUERY TOOL
=============================================
  [1] OpenAI  (via OpenRouter)
  [2] Groq    (LLaMA 3.1)
  [3] Ollama  (Local TinyLlama)
  [4] Hugging Face (DeepSeek)
  [5] Cohere  (command-r7b)
  [q] Quit
=============================================
Select provider (1-5) or q to quit:
```

---

## Screenshots of Working Programs

All programs tested and working. Screenshots are in the `screenshots/` folder.

| Program | Screenshot | Prompt Used |
|---|---|---|
| openai_example.py | openai_output.png | "what is computer Networks?" |
| groq_example.py | groq_output.png | "what is Ai?" |
| ollama_example.py | ollama_output.png | "what is Deep learning give an example?" |
| huggingface_example.py | huggingface_output.png | "what is IT?" |
| cohere_example.py | cohere_output.png | "what is Machine Learning?" |
| multi_api_query.py | multi_api_query_output(1-6).png | All 5 providers tested |

---

## Key Implementation Highlights

- ✅ **Environment variables** used for all API keys via `os.getenv()`
- ✅ **Error handling** with `try/except` in every program
- ✅ **Clean, commented code** with docstrings
- ✅ **Ollama runs offline** — no internet needed after model download
- ✅ **Cohere uses new Chat API** — migrated from deprecated Generate API
- ✅ **HuggingFace uses InferenceClient** — modern approach with `provider="auto"`
- ✅ **OpenAI uses OpenRouter** — free alternative since OpenAI removed free tier
- ✅ **Bonus multi_api_query.py** — unified tool for all 5 providers

---

## Requirements

```
openai>=1.0.0
groq>=0.4.0
requests>=2.31.0
google-generativeai>=0.5.0
cohere>=5.0.0
huggingface_hub>=0.20.0
```

---

## Submission Checklist

- [1] All 5 API programs created and working
- [2] Each program accepts user input
- [3] Each program displays AI responses correctly
- [4] Error handling implemented in all programs
- [5] requirements.txt file included
- [6] README.md complete with setup instructions
- [7] Screenshots of all programs included
- [8] API keys use os.getenv() — not hardcoded in logic
- [9] All files committed to GitHub
- [10] Repository set to PUBLIC
- [11] Bonus: multi_api_query.py implemented with all 5 providers


Name : Harshith K S
Course : "Generative AI"
Institution : "CampusPe"
Mentor : "Jacob Dennis"
Year : "2026"