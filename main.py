from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
api_url = os.getenv("OLLAMA_API_URL")
model=os.getenv("OLLAMA_MODEL")
client = OpenAI(api_key=api_key, base_url=api_url)


numero_dias = 5
numero_criancas = 2
atidades = "parques, museus e atividades ao ar livre"
cidade = "Lisboa"

prompt = f"""
            Crie um roteiro de viagem de {numero_dias} dias para uma familia {numero_criancas} crianças, 
            que gosta de {atidades}, e que vai viajar para {cidade}.
            """


response=client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "Você é um assistente de viagem especializado em criar roteiros personalizados."},
        {"role": "user", "content": prompt}
    ]
)

print("Roteiro de viagem gerado com sucesso!")
print(f"Prompt enviado para o modelo:\n{prompt}")
resposta_em_texto = response.choices[0].message.content
print(f"Resposta do modelo:\n{resposta_em_texto}")


