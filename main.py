from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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


modelo_prompt = PromptTemplate(template="Sugira uma cidade dado o meu interesse por {interesse}."
                               , input_variables=["interesse"])

interesse="praias"
prompt_cidade=modelo_prompt.format(interesse=interesse)
print(f"\nPrompt gerado: {prompt_cidade}\n")
modelo=ChatOpenAI(model=model,
                  temperature=0.5,
                  base_url=api_url,
                  api_key=api_key)

cadeia=modelo_prompt | modelo | StrOutputParser()
resposta=cadeia.invoke({
    "interesse": interesse
})

print(resposta)

