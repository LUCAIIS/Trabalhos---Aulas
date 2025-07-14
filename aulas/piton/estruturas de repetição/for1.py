numero = int(input("Digite um número: "))
print(f"Tabuada do numero {numero}:")
for vezes in range(11):
    resultado = numero * vezes
    print(f"_"*10)
    print (f"{numero} X {vezes} = {resultado}")