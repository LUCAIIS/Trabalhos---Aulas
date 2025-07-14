numero1 =float(input("digite o numero 1:"))
numero2 =float(input("Digite o numero 2: "))
opercao = input("digite a operação: (+ , - , * , / )")
if (opercao == "+"):
    resultado = numero1 + numero2 
    print(f"O resultado da soma {numero1} + {numero2} = {resultado}")
elif(opercao == "-"):
    resultado = numero1 - numero2
    print(f"O resultado da subtração {numero1} + {numero2} = {resultado}")
elif(opercao == "*"):
    resultado = numero1 * numero2
    print(f" O resultado da multiplicação {numero1} * {numero2} = {resultado}")
elif(opercao=="/"):
    resultado = numero1 / numero2
    print(f" O resultado da Subtração:{numero1} / {numero2} = {resultado:.2f}")
else:
    print("O usuario foi incompetende de escrever algo que o meu codigo supremo nao reconhece")