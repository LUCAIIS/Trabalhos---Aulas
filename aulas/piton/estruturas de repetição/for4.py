media = 0
quantidade = int(input("Digite a quantidade de pessoas: "))
for i in range(quantidade):
    nome = input("Digite o nome da pessoas cadastrada: ")
    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite o se peso: "))
    imc = peso/altura**2
    media+=imc
    print(f"O IMC do Usuario {nome} é {imc:.2f}")
mediageral = media / quantidade
print(f"A media geral do IMC é de {mediageral:.2f}")
