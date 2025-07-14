valor = float(input("Digite o valor da sua compra: "))
if valor <= 100:
    desconto = 0
elif valor <= 300:
    desconto = 0.10
elif valor <= 500:
    desconto = 0.15
else:
    desconto = 0.20
valordesconto = valor*desconto
total = valor - valordesconto
print(f"O valor sem desconto é de {valor:.2f}")
print(f"Voce recebeu um desconto de {valordesconto:.2f}")
print(f"O Valor com desconto foi de {total:.2f}")