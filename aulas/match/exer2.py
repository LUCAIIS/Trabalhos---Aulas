mes = int(input("Digite um numero (1 a 12): "))
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Número inválido")
