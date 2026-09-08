# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no BraatFinanças? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores ou seja, dar continuidade ao atendimento de forma mais eficiente.  |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidades de aprendizado do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser explicados ao clientes  |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didatica |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O Produto Fundo Imobiliário (FII) substitui o Fundo Multimercado, pois prefiro usar apenas produtos financeiros que eu conheço.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
