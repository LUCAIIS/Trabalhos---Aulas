import os
quantidade = 0
soma = 0
valor = -1
while valor != 0:
    valor = float(input("Digite um numero Real: "))
    if valor != 0:
        quantidade += 1
        soma += valor
    os.system('cls')
print(f"Foram Digitados: {quantidade}")
print(f"Media dos numeros digitados: {soma/quantidade:.2f}")