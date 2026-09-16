import json
import os
import pandas as pd
import requests
import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Braat Finanças",
                   page_icon="💰", layout="centered")

# =========== CONFIGURAÇÃO GEMINI ===========
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = "gemini-3.6-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={GEMINI_API_KEY}"

# =========== CARREGAR DADOS ===========
with open('./data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

transacoes = pd.read_csv('./data/transacoes.csv', encoding='utf-8')
historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')

with open('./data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)

# =========== MONTAR CONTEXTO ===========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM PROMPT ===========
SYSTEM_PROMPT = """Você é o Braat Finanças, um mentor e educador financeiro pessoal amigável, didático e focado em segurança.

OBJETIVO:
Capacitar o cliente a entender seu dinheiro e ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos para decisões financeiras conscientes.

REGRAS:
- NUNCA recomende investimentos específicos nem faça promessas de retorno garantido, apenas explique didaticamente como cada produto funciona;
- Priorize sempre a Reserva de Emergência antes de abordar qualquer investimento com risco ou baixa liquidez;
- NUNCA solicite, armazene ou aceite senhas, dados de cartão, contas bancárias ou chaves PIX;
- JAMAIS responda a perguntas fora do tema de finanças pessoais. Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados do cliente fornecidos no contexto para dar exemplos práticos e personalizados;
- Use linguagem simples, empática e acessível, como se explicasse para um amigo;
- Se não souber algo, admita com transparência: "Não tenho essa informação no momento, mas posso te explicar...";
- Sempre pergunte se o cliente entendeu ao final da explicação;
- Responda de forma sucinta, acolhedora e direta, com no máximo 3 parágrafos.
"""

# =========== FUNÇÃO DE CHAMADA GEMINI ===========


def perguntar(msg, chave_ativa):
    prompt_completo = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta do usuário: {msg}"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={chave_ativa}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt_completo}]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 800
        }
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        dados = response.json()

        if "candidates" in dados and len(dados["candidates"]) > 0:
            return dados["candidates"][0]["content"]["parts"][0]["text"]
        elif "error" in dados:
            return f"❌ **Erro na API do Gemini:** {dados['error'].get('message', dados['error'])}"
        else:
            return f"⚠️ Resposta inesperada: {dados}"

    except Exception as e:
        return f"❌ Erro de conexão: {str(e)}"


# =========== INTERFACE STREAMLIT ===========
st.title("💰 Braat Finanças - Seu Mentor Financeiro")

with st.sidebar:
    st.header("⚙️ Configurações")
    chave_input = st.text_input(
        "Gemini API Key:", value=GEMINI_API_KEY, type="password")

if pergunta := st.chat_input("Digite sua dúvida sobre finanças, orçamento ou investimentos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Braat Finanças analisando..."):
        chave_usar = chave_input if chave_input else GEMINI_API_KEY
        if not chave_usar:
            st.chat_message("assistant").write(
                "⚠️ Por favor, insira sua **Gemini API Key** na barra lateral à esquerda para começar!")
        else:
            resposta = perguntar(pergunta, chave_usar)
            st.chat_message("assistant").write(resposta)
