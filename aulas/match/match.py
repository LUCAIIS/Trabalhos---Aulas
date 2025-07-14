dia = int(input("Digite um numero (1 a 7): "))
match dia:
    case 1:
        print("Segunda-Feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-Feira")
    case 4:
        print("Quinta-Feira")
    case 5:
        print("Sexta-Feira")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _ :
        print("Numero invalido")
