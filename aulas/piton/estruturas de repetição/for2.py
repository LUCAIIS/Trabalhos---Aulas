soma = 0
quantidade = 0
for i in range(1, 10000):
    if (i%2 != 0) and (i%3 == 0):
        print("numero ", i)
        soma+=i
        quantidade+=i
print(f"soma = {soma}")
print(f"Repetiu = {quantidade}")