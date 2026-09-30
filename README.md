# 🐍 Exercícios de Tuplas e Dicionários em Python

Repositório com exercícios de Python focados no uso de **tuplas** e **dicionários**, explorando criação, acesso, iteração, atualização de valores, agrupamento por chave e formatação de saída.

## Índice
- [a) Dicionário de quadrados]
- [b) Soma por categoria]
- [c) Lista telefônica]
- [d) Agrupando por letra]
- [e) Contagem de letras na frase]
- [f) Salários e valores]

## a) Dicionário de quadrados:
Cria um dicionário onde as chaves vão de `1` até `n` e os valores são os quadrados das chaves. Trabalha **criação de dicionário**, **iteração com `range`** e **preenchimento de pares chave-valor**. Também apresenta uma versão com **dict comprehension**, mostrando como montar o mesmo dicionário em uma única linha.

## b) Soma por categoria:
Recebe `n` pares de categoria e valor, e soma os valores agrupando por categoria. Trabalha **leitura com `split()`**, **verificação de existência de chave**, **atualização incremental de valores** e o uso de **`.get(chave, padrão)`** para simplificar o código. Explora também a **ordem de inserção** mantida pelos dicionários a partir do Python 3.7.

## c) Lista telefônica:
Cadastra nomes e telefones até o usuário digitar `"fim"`, e depois consulta um nome específico. Trabalha **leitura em loop com condição de parada**, **normalização com `.lower()`** para ignorar maiúsculas/minúsculas, **consulta em dicionário** e **tratamento de chave inexistente** com mensagem personalizada. Apresenta também uma versão com **walrus operator** e `.get()`.

## d) Agrupando por letra:
Agrupa nomes pela primeira letra (ignorando maiúsculas/minúsculas) e exibe os grupos em ordem alfabética, preservando a ordem de inserção dentro de cada grupo. Trabalha **dicionários com listas como valores**, **`.append()`**, **ordenação de chaves com `sorted()`** e **junção de listas com `' '.join()`**. Também mostra a versão com **`defaultdict(list)`**.

## e) Contagem de letras na frase:
Conta quantas vezes cada letra aparece em uma frase, ignorando espaços, pontuação e diferenças entre maiúsculas e minúsculas. Trabalha **iteração sobre strings**, **filtro com `.isalpha()`**, **normalização com `.upper()`**, **`defaultdict(int)`** para contadores automáticos e **ordenação alfabética**. Inclui também uma versão com `unicodedata` para o caso de se querer **remover acentos**, e uma versão com **`Counter`**.

## f) Salários e valores:
Lê CPF, nome e salário de 10 funcionários e exibe quem está **abaixo** e **acima** da média, nessa ordem, separados em duas seções. Trabalha **listas de tuplas**, **ordem de inserção**, **cálculo de média com `sum()`**, **filtragem por condição** e **formatação de saída em blocos com separação em branco**. Reforça a diferença entre `<` e `>` (e o caso de empate com a média exata).
