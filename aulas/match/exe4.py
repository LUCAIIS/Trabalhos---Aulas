temperatura = float(input("Digite a temperatura em graus Celsius: "))
info = int(input("Escolha para qual medida quer converter (1 – Converter para Fahrenheit, 2 – Converter para Kelvin): "))
match info:
    case 1:
        final = (temperatura * 1.8) + 32
        print(f"A temperatura em Fahrenheit será de {final}F")
    case 2:
        final = temperatura +  273,15
        print(f"A temperatura em Kelvin seré de {final}K")
    case _:
        print("Operação invalida")