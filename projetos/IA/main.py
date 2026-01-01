from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Obtém a chave do .env
api_key = os.getenv("HF_API_KEY")

# Cria o cliente correto
client = InferenceClient(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    token=api_key
)

pergunta = input('Pergunta: ')

# Faz a consulta usando chat_completion
response = client.chat_completion(
    messages=[
        {"role": "user", "content": pergunta}
    ],
    max_tokens=200
)

print(response.choices[0].message["content"])
