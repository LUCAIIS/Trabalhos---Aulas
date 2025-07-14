import os
import colorama
colorama.init()
saldo = 0
continuar = ""
while continuar != "1":
    print(colorama.Fore.CYAN+"BANDO LUCAS"+colorama.Fore.RESET)
    print(colorama.Fore.GREEN+"_"*40)
    print(colorama.Fore.YELLOW+"(a) Consultar saldo")
    print("(b) sacar")
    print("(c) depositar")
    print("(d) sair"+colorama.Fore.WHITE)
    resposta = input("Digite a sua opção: ")
    os.system('cls')
    match resposta:
        case "a":
            print(f"Saldo atual:{saldo:.2f}")
            input("Digite <enter> Para proseguir")
        case "b":
            saque = float(input("Digite o valor que deseja sacar: "))
            saldo-= saque
        case "c":
            deposito = float(input("Digite o valor do deposito: "))
            saldo += deposito
        case "d":
            print("Sistema finalizado")
            print(f"Saldo Final:{saldo:.2f}")
            continuar = "1"
        case _:
            print("Error")
