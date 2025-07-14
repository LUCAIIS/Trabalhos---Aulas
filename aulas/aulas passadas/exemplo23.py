altura = float(input("Digite o sua altuta: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura ** 2)
if imc <= 18.05:
    print("Abaixo do peso")
elif imc <= 24.09:
    print("Peso normal")
elif imc <= 29.09:
    print("Sobrepeso")
elif imc <= 39.9:
    print("Obesidade")
elif imc < 40 :
    print("Obesidade Grave")