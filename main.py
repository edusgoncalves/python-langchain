from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
api_url = os.getenv("OLLAMA_API_URL")
model=os.getenv("OLLAMA_MODEL")


# Limpeza da tela
if os.name == 'nt':
    subprocess.run(['cmd', '/c', 'cls'])
else:
    subprocess.run(['clear'])


if not api_url or not api_url.strip():
    raise ValueError("A url da API não foi definida no .env")

print("URL carregada com sucesso!")

if not api_key or not api_key.strip():
    raise ValueError("A chave da API não foi definida no .env")

print("Chave da API carregada com sucesso!")

if not model or not model.strip():
    raise ValueError("O modelo não foi definido no .env")

print("Modelo carregado com sucesso!")

numero_dias = 5
numero_criancas = 2
atividades = "praia"
cidade = "Lisboa"

modelo_prompt = PromptTemplate.from_template("""
                                    Crie um roteiro de viagem de {dias} dias,
                                    para uma familia com {numero_criancas} criancas,
                                    que gostam de {atividade}
                                """)

prompt=modelo_prompt.format(dias=numero_dias,
                              numero_criancas=numero_criancas,
                              atividade=atividades)
print(f"Prompt gerado: {prompt}\n")

modelo=ChatOpenAI(model=model,
                  temperature=0.5,
                  base_url=api_url,
                  api_key=api_key)


resposta=modelo.invoke(prompt)

print(resposta.content)

