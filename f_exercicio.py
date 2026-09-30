# Salários e Valores

funcionarios = []

for _ in range(10):
    cpf = input()
    nome = input()
    salario = float(input())
    funcionarios.append((cpf, nome, salario))

media = sum(f[2] for f in funcionarios) / 10

print("Abaixo da média:")
for cpf, nome, salario in funcionarios:
    if salario < media:
        print(f"{cpf} {nome}")

print()
print("Acima da média:")
for cpf, nome, salario in funcionarios:
    if salario > media:
        print(f"{cpf} {nome}")