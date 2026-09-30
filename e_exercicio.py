# Contagem de letras na frase

from collections import defaultdict

frase = input()

contagem = defaultdict(int)

for caractere in frase:
    if caractere.isalpha():
        contagem[caractere.upper()] += 1

for letra in sorted(contagem):
    print(f"{letra}: {contagem[letra]}")