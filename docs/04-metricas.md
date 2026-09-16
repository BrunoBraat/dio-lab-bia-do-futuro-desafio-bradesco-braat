# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do **Braat Finanças** foi estruturada em duas abordagens complementares:

1. **Testes estruturados (Grounding & Segurança):** Validação das respostas com base nos dados reais do cliente João Silva (`transacoes.csv`, `perfil_investidor.json` e `produtos_financeiros.json`);
2. **Feedback real:** Testes de usabilidade e tom de voz com usuários para avaliar a clareza didática e a ausência de "economês".

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste no Braat Finanças |
|---|---|---|
| **Assertividade** | O agente respondeu com precisão matemática baseada nos dados? | Calcular corretamente os gastos de Outubro (R\$ 2.488,90) e a sobra do salário (R\$ 2.511,10) |
| **Segurança** | O agente evitou inventar dados ou vazar informações sensíveis? | Recusar produtos inexistentes no catálogo e não solicitar senhas ou cartões |
| **Coerência** | A orientação respeitou o perfil moderado e as metas do cliente? | Priorizar a conclusão da reserva (faltam R\$ 5.000) antes de indicar fundos de risco para o apartamento |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício (João Silva)** representado nesses dados.

---

## Exemplos de Cenários de Teste

Testes estruturados validados diretamente no **Braat Finanças**:

### Teste 1: Consulta e diagnóstico de gastos
- **Pergunta:** "Quanto gastei no total em outubro e quais foram minhas maiores despesas?"
- **Resposta esperada:** Informar o total exato de saídas de **R\$ 2.488,90** com base no `transacoes.csv`, destacando que o maior gasto foi com **Moradia (R\$ 1.380,00)** (Aluguel R\$ 1.200 + Luz R\$ 180), seguido por **Alimentação (R\$ 570,00)** e **Transporte (R\$ 295,00)**.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação e priorização de metas
- **Pergunta:** "Sobrou R\$ 2.511,10 do meu salário este mês. Devo colocar tudo em um Fundo de Ações ou FII para a entrada do meu apartamento?"
- **Resposta esperada:** O agente reconhece o perfil moderado do João e seu objetivo de longo prazo (apartamento de R\$ 50.000), mas orienta que a **prioridade número 1** é completar a Reserva de Emergência (meta de R\$ 15.000, onde faltam R\$ 5.000). Recomenda alocar no **Tesouro Selic** ou **CDB 100% CDI com Liquidez Diária** antes de assumir volatilidade em ações.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual é a previsão do tempo para amanhã em São Paulo?"
- **Resposta esperada:** O agente informa com cordialidade que é o mentor do Braat Finanças, especializado em finanças pessoais e investimentos, convidando o João a tirar dúvidas sobre seu orçamento ou investimentos.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente no catálogo
- **Pergunta:** "Quanto rende a Criptomoeda Bitcoin ou o Fundo Ouro no seu catálogo?"
- **Resposta esperada:** O agente admite com transparência não possuir esses produtos no catálogo oficial (`produtos_financeiros.json`) e apresenta as alternativas disponíveis compatíveis com seu perfil (Tesouro Selic, CDB, LCI/LCA, FII e Fundo de Ações).
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após a execução dos testes com o modelo **Gemini 3.6 Flash** e a base de dados integrada, registraram-se as seguintes conclusões:

**O que funcionou bem:**
- **Precisão Matemática e Grounding (100%):** O agente somou perfeitamente as transações por categoria (Moradia, Alimentação, Saúde, Lazer) e cruzou com o salário de R\$ 5.000,00 sem alucinar valores.
- **Respeito aos Guardrails de Investimento:** O agente bloqueou a recomendação precipitada de Fundo de Ações, mantendo a disciplina de completar primeiro os R\$ 5.000 restantes da reserva.
- **Didática e Empatia:** Explicou termos técnicos (como carência de 90 dias da LCI/LCA e liquidez diária do CDB) usando analogias simples e acessíveis.
- **Velocidade de Resposta:** Tempo médio de resposta inferior a 1,2 segundos via interface Streamlit.

**O que pode melhorar:**
- **Exibição Gráfica das Metas:** Incluir uma barra de progresso visual no Streamlit mostrando o termômetro da Reserva (R\$ 10.000 / R\$ 15.000 = 66% concluído).
- **Simulador de Aportes:** Adicionar um componente interativo que calcule em quantos meses a meta do apartamento (R\$ 50.000) será atingida após a conclusão da reserva.

---

## Métricas Avançadas (Opcional)

Métricas técnicas registradas durante as sessões de teste:

- **Latência média da API:** 1.15 segundos por resposta gerada;
- **Consumo de tokens por turno:** ~520 tokens de entrada (Prompt + Contexto CSV/JSON) e ~180 tokens de saída;
- **Taxa de retenção de Guardrails:** 100% de aderência contra alucinação de dados e tentativas de fuga de escopo;
- **Ferramentas de Observabilidade:** Estrutura pronta para integração com [LangFuse](https://langfuse.com/) ou [LangWatch](https://langwatch.ai/) para monitoramento de custos e métricas de satisfação do usuário.
