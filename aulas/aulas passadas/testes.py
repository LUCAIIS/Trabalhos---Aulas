import os
valor_em_banco = 0
while True:
    print("1 - Depositar Dinheiro\n2 - Sacar Dinheiro\n3 - Investir Dinheiro\n4 - Visualizar Saldo\n5 - Visualizar Investimentos\n6 - Encerrar ")
    opcao = int(input("Digite o numero da Opção desejada: "))
    os.system('cls')
    match opcao:
        case 1:
            valor_deposito = float(input("Digite o valor que deseja Depositar: "))
            confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar deposito! ")
            if confirmacao == "1":
                valor_em_banco += valor_deposito
                os.system('cls')
                print("Valor Depositado! ")
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                match continuar:
                    case 1:
                        continue
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                        break

            elif confirmacao == "2":
                print("Processo interrompido!")
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                match continuar:
                    case 1:
                        continue
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                        break

            else:
                print("O programa nao consguir ser bom o bastante para tamanha burrice! ")
        case 2:
            print(f"Saldo em banco: {valor_em_banco}")

        case _:
            print("Algo de errado")     
            