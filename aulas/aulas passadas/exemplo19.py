quantidade = int(input("Quantas notas voce teve? "))
soma = 0
for i in range(quantidade):
#esse i pode ser substituudo por utra coisa, ele é tipo de um marco que mostra quantas vezez foi repetido o codigo, nao sei se é exatemente isso
    notas= float(input(f"Qual o valor da sua nota?"))
    soma = soma + notas
media = soma/quantidade
if media >= 6:
    print("Aprovado!")
elif media < 6:
    print("Reprovado")
else:
    print("O numero nao é invalido")