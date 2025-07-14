frequencia = int(input("Quantas faltas você teve? "))
quantidade = int(input("São quantas notas?"))
lista = []
for i in range (quantidade):
    nota = float(input(f"Qual foi a nota {i + 1}: "))
    lista.append(nota)
print("Notas digitadas: ", lista)
soma = sum(lista)
media = soma/len(lista)
print("A sua média foi de:", media)
if 7 <= media and 25 >= frequencia:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado")