from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
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


class Restaurantes(BaseModel):
    cidade: str = Field(..., description="Cidade sugerida para o interesse do usuário")
    restaurantes: str = Field(..., description="Restaurantes recomendados na cidade sugerida") 

parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)

prompt_cidades = PromptTemplate(template="""
Sugira uma cidade dado o meu interesse por {interesse}.
Responda com uma sugestão concreta e explique por que essa cidade atende ao interesse.
{formato_saida}
Retorne somente o objeto JSON preenchido com os campos "cidade" e "motivo".
Não retorne o esquema JSON nem campos como "properties" ou "required".
Exemplo de resposta para interesse em museus:
{{"cidade": "Paris", "motivo": "Possui museus como o Louvre e o Musée d'Orsay."}}
"""
                               , input_variables=["interesse"],
                               partial_variables={"formato_saida": parseador_destino.get_format_instructions()})
prompt_restaurantes = PromptTemplate(template="""
Sugira restaurantes populares na cidade {cidade}
{formato_saida}
Retorne somente o objeto JSON preenchido com os campos "cidade" e "restaurantes".
Não retorne o esquema JSON nem campos como "properties" ou "required".
Exemplo de resposta para interesse em museus:
{{"cidade": "Paris", "restaurantes": "Osteria del Circo, La Pergola, Armando al Pantheon"}}
"""
                               , input_variables=["cidade"],
                               partial_variables={"formato_saida": parseador_restaurantes.get_format_instructions()})

prompt_cultural = PromptTemplate(template="""
Sugira atividades e locais culturais em {cidade} exiba os {restaurantes}
""")



modelo=ChatOpenAI(model=model,
                  temperature=0.5,
                  base_url=api_url,
                  api_key=api_key)


cadeia_1=prompt_cidades | modelo |parseador_destino
cadeia_2=prompt_restaurantes|modelo|parseador_restaurantes
cadeia_3=prompt_cultural|modelo|StrOutputParser()
cadeia=cadeia_1|cadeia_2|cadeia_3
print("\nConsultando o Ollama; aguarde a geração da resposta...", flush=True)
resposta=cadeia.invoke({
    "interesse": "praia"
})
print(f"\nResposta: {resposta}\n")


