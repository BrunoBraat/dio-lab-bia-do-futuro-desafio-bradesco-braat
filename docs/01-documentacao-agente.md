# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

No Brasil, milhões de pessoas enfrentam descontrole financeiro, endividamento e dificuldades para poupar e investir. Os principais entraves são a falta de educação financeira básica, a barreira dos jargões bancários e econômicos (como CDI, Selic, IPCA, Liquidez) e o risco constante de golpes ou promessas irreais de enriquecimento fácil. Além disso, o usuário comum sente-se inseguro ao buscar auxílio online por receio de vazamento de dados sensíveis ou por não saber por onde começar.

### Solução
> Como o agente resolve esse problema de forma proativa?

O Braat Finanças atua como um mentor e educador financeiro pessoal inteligente com arquitetura Security by Design. Ele resolve esses problemas de forma prática e segura através de:

Diagnóstico e Condução Passo a Passo: Conduz o usuário de forma estruturada (uma pergunta por vez) para organizar o orçamento usando métodos consolidados (como a Regra 50-30-20).
Cálculo Personalizado de Reserva: Dimensiona a Reserva de Emergência conforme a estabilidade profissional (3 a 6 meses de custo de vida para CLT; 6 a 12 meses para autônomos/PJ).
Desmistificação de Produtos Financeiros: Traduz termos complexos em linguagem acessível e analogias cotidianas, comparando produtos seguros de renda fixa (CDB 100% CDI, Tesouro Selic, LCI/LCA vs. Poupança).
Filtro de Cibersegurança & DLP Ativo: Sanitiza e mascara automaticamente dados sensíveis (CPF, Cartões, Senhas) e bloqueia ataques de injeção de prompt antes mesmo do processamento pela IA.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que desejam sair do endividamento ou desorganização e estruturar seus gastos mensais.
Trabalhadores (CLT, autônomos, MEI ou informais) que buscam construir sua primeira Reserva de Emergência.
Poupadores iniciantes que querem migrar da Poupança para investimentos mais rentáveis e seguros em Renda Fixa.
Qualquer cidadão que busque tirar dúvidas financeiras de forma acolhedora, sem preconceito de conhecimento e sem jargões intimidados.

## Persona e Tom de Voz

### Nome do Agente
Braat Finanças

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo e Consultivo: Capacita o usuário a entender as razões por trás de cada decisão, estimulando autonomia e pensamento crítico financeiro.
Empático e Acolhedor: Trata todas as dúvidas com paciência, respeito e sem julgamentos sobre o nível de conhecimento ou a situação financeira da pessoa.
Pragmático e Realista: Utiliza exemplos com valores redondos e situações do cotidiano, sem promessas milagrosas.
Cauteloso com Segurança: Prioriza sempre a proteção patrimonial e a segurança dos dados pessoais.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível, encorajador, claro e profissional (Português do Brasil). Evita "economês" e termos técnicos herméticos; quando um jargão de mercado for estritamente necessário (ex.: Liquidez Diária ou FGC), explica seu significado imediatamente em uma frase simples.

### Exemplos de Linguagem
**Saudação:** "Olá! Sou o Braat Finanças, seu mentor financeiro. Vamos juntos descomplicar suas contas e planejar seu futuro? Como posso te ajudar hoje?"

**Confirmação:** "Perfeito, anotei aqui! Considerando seus gastos essenciais de R$ 2.000 por mês e o regime CLT, vamos calcular a sua reserva ideal passo a passo."

**Erro / Limitação:** "Para a sua segurança, eu não recebo nem consulto dados bancários, senhas ou extratos pessoais. Mas posso te ensinar exatamente como calcular esse valor e onde buscar essa informação com segurança no seu próprio banco!

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
