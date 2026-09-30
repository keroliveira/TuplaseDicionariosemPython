# Dicionário de Quadrados

n = int(input())

quadrados = {}
for i in range(1, n + 1):
    quadrados[i] = i ** 2

for chave, valor in quadrados.items():
    print(f"{chave}: {valor}")