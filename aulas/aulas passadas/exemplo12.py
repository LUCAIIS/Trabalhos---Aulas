
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso/(altura **2)
if 18.5 > imc:
    print("voce esta abaixo do peso")
if 22.4 < imc:
    print("voce esta acima do peso")
if 22.4 >= imc >= 18.5:
    print("voce esta com o peso ideal")
    #esse codigo pode ser feito usando o elif ok?
