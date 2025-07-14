import os
valor_em_banco = 0
while True:
    print("1 - Depositar Dinheiro\n2 - Sacar Dinheiro\n3 - Emprestimo\n4 - Visualizar Saldo\n5- Encerrar ")
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
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
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
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
            else:
                print("O programa nao consguir ser bom o bastante para tamanha burrice! ")
        case 2:
            print(f"Saldo em banco: {valor_em_banco}")
            valor_sacar = float(input("Digite o valor que deseja sacar: "))
            if valor_sacar > valor_em_banco:
                print("O valor exedeu a quantidade em conta! ")
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                match continuar:
                    case 1:
                        continue
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                        break
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
                print("limite Exedido!\n")
            confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar deposito! ")
            if confirmacao == "1":
                valor_em_banco -= valor_sacar
                os.system('cls')
                print("Valor Sacado! ")
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                match continuar:
                    case 1:
                        continue
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                        break
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
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
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
        case 3:
            score = valor_em_banco*10
            print(f"O seu limite é definito em relação ao valor em banco!\nO seu limite é de:{score}")
            if score <= 0:
                print("Você não valor disponivel para emprestimo")
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                match continuar:
                    case 1:
                        continue
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                        break
                    case _:
                        print("Erro - Retornando ao menu")
                        continue
            else:
                valor_emprestimo = float(input("Qual o valor do emprestimo? "))
                confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar emprestimo! ")
                if confirmacao == "1":
                    valor_em_banco += valor_emprestimo
                    os.system('cls')
                    print("Valor Recebido! ")
                    continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
                    match continuar:
                        case 1:
                            continue
                        case 2: 
                            os.system('cls')
                            print("Programa encerrado")
                            break
                        case _:
                            print("Erro - Retornando ao menu")
                            continue
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
                        case _:
                            print("Erro - Retornando ao menu")
                            continue
                    
        case 4: 
            print(f"Valor em banco: {valor_em_banco}") 
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa"))
            match continuar:
                case 1:
                    continue
                case 2: 
                    os.system('cls')
                    print("Programa encerrado")
                    break
                case _:
                    print("Erro - Retornando ao menu")
                    continue 
        case 5:
            os.system('cls')
            print("Programa encerrado!")
            break
        case _:
            print("Erro - Retornando ao menu")
            continue