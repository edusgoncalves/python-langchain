<img width="989" alt="image" src="https://github.com/user-attachments/assets/c140d5f9-a165-44d0-80b9-592fdbf16e03" />


# LangChain e Python: criando ferramentas com LLM via Ollama

Este projeto utiliza **Ollama em vez da OpenAI** para executar o modelo de linguagem. O código mantém a classe `ChatOpenAI`, da biblioteca `langchain-openai`, para acessar a API compatível com OpenAI disponibilizada pelo Ollama.

## ⚙️ Guia de Configuração

Siga os passos abaixo para configurar seu ambiente e utilizar os scripts do projeto.

### 1. Criar e Ativar Ambiente Virtual

**Windows:**
```bash
python -m venv langchain
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv langchain
source langchain/bin/activate
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configurar o Ollama

Instale o [Ollama](https://ollama.com/download) para seu sistema operacional. Os comandos abaixo usam `llama3.2` como exemplo; substitua pelo modelo que deseja utilizar.

Confira a instalação e inicie o servidor caso ele ainda não esteja em execução:

```bash
ollama --version
ollama serve
```

Se iniciado pelo terminal, mantenha `ollama serve` rodando e abra outro terminal para os próximos comandos. Se o aplicativo ou serviço do Ollama já estiver ativo, não é necessário iniciar outro servidor.

Baixe o modelo e confira os modelos disponíveis:

```bash
ollama pull llama3.2
ollama list
```

Para testar uma conversa diretamente no terminal:

```bash
ollama run llama3.2
```

Digite `/bye` para sair da conversa. Para consultar os modelos carregados e liberar o modelo da memória:

```bash
ollama ps
ollama stop llama3.2
```

Crie ou edite o arquivo `.env` com as variáveis utilizadas em `main.py`:

```bash
OLLAMA_API_KEY="ollama"
OLLAMA_API_URL="http://localhost:11434/v1"
OLLAMA_MODEL="llama3.2"
```

Informe em `OLLAMA_API_URL` a URL base do endpoint compatível com OpenAI do seu servidor Ollama e, em `OLLAMA_MODEL`, o nome de um modelo disponível nesse servidor. Para um servidor local sem autenticação, use um valor como `ollama` em `OLLAMA_API_KEY`; se o servidor exigir autenticação, informe a chave correspondente.

Não é necessário configurar `OPENAI_API_KEY`. Mantenha o arquivo `.env` fora do controle de versão para proteger suas credenciais.

Referências: [documentação do Ollama](https://docs.ollama.com/quickstart) e [compatibilidade com OpenAI](https://docs.ollama.com/api/openai-compatibility).

### 4. Executar o Projeto

Com o servidor Ollama ativo, o modelo baixado e o ambiente virtual ativado, execute:

```bash
python main.py
```

O script enviará o prompt ao Ollama e exibirá o roteiro de viagem no terminal.
