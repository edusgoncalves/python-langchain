from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.globals import set_debug
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
api_url = os.getenv("OLLAMA_API_URL")
model=os.getenv("OLLAMA_MODEL")

set_debug(False)

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


class Destino(BaseModel):
    cidade: str = Field(..., description="Cidade sugerida para o interesse do usuário")
    motivo: str = Field(..., description="Motivo pelo qual a cidade foi sugerida") 


parseador = PydanticOutputParser(pydantic_object=Destino)

prompt_modelo = PromptTemplate(template="""
Sugira uma cidade dado o meu interesse por {interesse}.
Responda com uma sugestão concreta e explique por que essa cidade atende ao interesse.
{formato_saida}
Retorne somente o objeto JSON preenchido com os campos "cidade" e "motivo".
Não retorne o esquema JSON nem campos como "properties" ou "required".
Exemplo de resposta para interesse em museus:
{{"cidade": "Paris", "motivo": "Possui museus como o Louvre e o Musée d'Orsay."}}
"""
                               , input_variables=["interesse"],
                               partial_variables={"formato_saida": parseador.get_format_instructions()})


modelo=ChatOpenAI(model=model,
                  temperature=0.5,
                  base_url=api_url,
                  api_key=api_key)

cadeia=prompt_modelo | modelo | parseador
print("\nConsultando o Ollama; aguarde a geração da resposta...", flush=True)
resposta=cadeia.invoke({
    "interesse": "praia"
})
print(f"\nCidade: {resposta.cidade}")
print(f"Motivo: {resposta.motivo}")

