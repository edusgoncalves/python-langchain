from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
api_url = os.getenv("OLLAMA_API_URL")
model=os.getenv("OLLAMA_MODEL")

numero_dias = 5
numero_criancas = 2
atidades = "praia"
cidade = "Lisboa"

prompt = f"""
            Crie um roteiro de viagem de {numero_dias} dias para uma familia {numero_criancas} crianças, 
            que gosta de {atidades}, e que vai viajar para {cidade}.
            """


modelo=ChatOpenAI(model=model,
                  temperature=0.5,
                  base_url=api_url,
                  api_key=api_key)


resposta=modelo.invoke(prompt)

print(resposta.content)

