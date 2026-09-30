# Soma por categoria

n = int(input())

somas = {}
for _ in range(n):
    linha = input().split()
    categoria = linha[0]
    valor = int(linha[1])
    
    if categoria in somas:
        somas[categoria] += valor
    else:
        somas[categoria] = valor

for categoria, total in somas.items():
    print(f"{categoria}: {total}")