intens= int(input("Quandos intens você comprou? "))
lista_valor = []
for i in range(intens):
    valor_solo = int(input(f"Qual o valor do {i +1}ª intem? "))
    lista_valor.append(valor_solo)
soma = sum(lista_valor)
if 100 <= soma or 10 <= intens:
    print("Parabéns! Você tem os requisitos para receber o desconto")
else:
    print ("Voce não tem os requisitos necessarios para o desconto")