```markdown
# 💻 Código da Aplicação - Braat Finanças

Esta pasta contém o código-fonte da aplicação interativa do **Braat Finanças**, desenvolvida em Python e Streamlit com integração à API do **Google Gemini** e suporte a modelos locais via Ollama.

## 📁 Estrutura da Pasta `src/`

```text
src/
├── app.py               # Aplicação principal com interface Streamlit e chamada à IA
├── requirements.txt     # Lista de dependências e bibliotecas necessárias
└── README.md            # Guia de execução e documentação técnica da aplicação
```

## 📦 Dependências (`requirements.txt`)

O projeto utiliza as seguintes bibliotecas Python:

```text
streamlit>=1.35.0
pandas>=2.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## 🚀 Como Rodar a Aplicação

Siga o passo a passo abaixo para executar o **Braat Finanças** localmente:

### 1. Clonar o repositório
```bash
git clone https://github.com/BrunoBraat/dio-lab-bia-do-futuro-desafio-bradesco-braat.git
cd dio-lab-bia-do-futuro-desafio-bradesco-braat
```

### 2. Instalar as dependências
```bash
pip install -r src/requirements.txt
```

### 3. Configurar a Chave de API (Google Gemini)
Você pode configurar a chave de duas formas:
- **Opção A (Recomendada):** Inserir a chave diretamente no campo **"Gemini API Key"** na barra lateral da aplicação web.
- **Opção B (Variável de Ambiente):**
  - No Windows (PowerShell): `$env:GEMINI_API_KEY="sua_chave_aqui"`
  - No Linux/macOS: `export GEMINI_API_KEY="sua_chave_aqui"`

### 4. Iniciar o Servidor Streamlit
Execute o comando a partir da raiz do projeto:

```bash
streamlit run src/app.py
```

A aplicação abrirá automaticamente no seu navegador no endereço `http://localhost:8501`.

## 🛡️ Recursos Implementados

- **Context Grounding:** Injeção automática dos dados do cliente (`perfil_investidor.json`, `transacoes.csv` e `produtos_financeiros.json`) no prompt de sistema da IA.
- **Interface Conversacional Fluida:** Chat interativo com componentes nativos do Streamlit (`st.chat_input` e `st.chat_message`).
- **Segurança e Privacidade:** Campo de senha protegido para a API Key e Guardrails no System Prompt que impedem a recomendação precipitada de investimentos de risco antes da formação da Reserva de Emergência.
```

---
