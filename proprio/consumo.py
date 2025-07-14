consumo = float(input("Digite a media em KM/L do veiculo: "))
valor = float(input("Digite o valor do combustivel ultilizado: "))
litrosdia = 94 / consumo
litrosmes = 1880 / consumo
litrosano = litrosmes * 12
valordia = litrosdia*valor
valormes = litrosmes*valor
valorano = valormes * 12
print(f"O consumo por dia é de {litrosdia:.2f}L")
print(f"O consumo por mes é de {litrosmes:.2f}L")
print(f"O consumo por ano é de {litrosano:.2f}L")
print(f"O gasto por dia é de R${valordia:.2f}")
print(f"O gasto por mês é de R${valorano:.2f}")
print(f"O gasto por mes é de R${valormes:.2f}")