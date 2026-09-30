# Agrupando por letra

grupos = {}

while True:
    nome = input()
    if nome == "fim":
        break
    letra = nome[0].upper()
    if letra not in grupos:
        grupos[letra] = []
    grupos[letra].append(nome)

for letra in sorted(grupos):
    print(f"{letra}: {' '.join(grupos[letra])}")