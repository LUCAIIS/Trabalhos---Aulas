numero1=int(input("DIgite o primeiro numero: "))
numero2=int(input("DIgite o segundo  numero: "))
numero3=int(input("DIgite o terceiro numero: "))
if numero1 > numero2 and numero3:
    print(f"o numero {numero1} é o maior deles.")
elif numero2 > numero1 and numero3:
    print(f"o numero {numero2} é o maior deles")
elif numero3 > numero1 and numero2:
    print(f"o numero  {numero3}, é o maior deles")
else:
    print("o numero é 0 ou nao se enquadra nos requisitos")