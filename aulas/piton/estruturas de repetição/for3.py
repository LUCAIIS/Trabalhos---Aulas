alunos = int(input("Qual a quantidade de alunos desja cadastrar: "))
soma = 0
for i in range(alunos):
    nome = input("Digite seu nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2
    soma+=media
    print(f"A media do Aluno {nome} foi de {media:.2f}")
    if media >= 7:
        print(f"Aluno {nome} Aprovado")
    else:
        print(f"Aluno {nome} Reprovado")
mediageral = soma / alunos
print(f"A Media geral dos alunos foi de: {mediageral:.2f}")