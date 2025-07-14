present=float(input("Quantos presentes foram comprados? "))
valor=float(input("Qual foi o valor de cada presente? ")) 
frete= 20
valortotal=present*valor


desconto= 0.05 * valortotal
valordesconto= valortotal - desconto
valorfrete = valordesconto + frete


print(f"O valor todal sem desconto foi de {valortotal}Reais")
print(f"O valor total com desconto foi de {valordesconto}Reais")
print(f"O valor total com desconto e com frete foi de {valorfrete}Reais")