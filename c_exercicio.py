# Lista telefônica

lista = {}

while True:
    linha = input()
    if linha == "fim":
        break
    nome, telefone = linha.split()
    lista[nome.lower()] = telefone

consulta = input().lower()

if consulta in lista:
    print(lista[consulta])
else:
    print("Essa pessoa não está na lista telefônica")