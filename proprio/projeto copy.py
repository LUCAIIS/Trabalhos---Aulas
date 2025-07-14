import time # foda dms, da pra dar tempo noq vai acontecer. 
extratoG = []
valor_banco = 0
total_investimentos = 0
mesespassados = 0
valor_investido = 0
import os
def menu():
    print("1 - Depositar Dinheiro\n2 - Sacar Dinheiro\n3 - Emprestimo\n4 - Visualizar Saldo\n" \
    "5 - Ivestimento\n6 - Status investimento\n7 - Extrato de Movimentações \n8 - Maquina do tempo\n9- Encerrar")
    try:
        opcao = int(input("Digite o numero da Opção desejada: "))
        os.system('cls')
        # isso é muito degal, mas é chato time.sleep(1)
    except:
        os.system('cls')
        print("Você não digitou um número!")
        print("Retornando ao menu")
        print("-"*36)
        menu()
        

    match opcao:
        case 1: depositar() 
        case 2: sacar()
        case 3: emprestimo()
        case 4: capital()
        case 5: investimento()
        case 6: status_investimento()
        case 7: extrato()
        case 8: maquina_tempo()
        case 9: finalizar()
        case _: erro()

def depositar():
    os.system('cls')
    global extratoG
    valor_deposito = float(input("Digite o valor que deseja Depositar: "))
    confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar deposito!\n")
    if confirmacao == "1":
        global valor_banco
        valor_banco+= valor_deposito
        extratoG.append(f"Deposito no valor de: R${valor_deposito}")
        os.system('cls')
        print("Valor Depositado! ")
        try:
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
        except:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
        match continuar:
            case 1:
                os.system('cls')
                menu()
            case 2: 
                os.system('cls')
                print("Programa encerrado")
            case _:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
    elif confirmacao == "2":
                print("Processo interrompido!")
                try:
                    continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
                except:
                    print("Erro - Retornando ao menu")
                    print("-"*36)
                    menu()
                match continuar:
                    case 1:
                        os.system('cls')
                        menu()
                    case 2: 
                        os.system('cls')
                        print("Programa encerrado")
                    case _:
                        print("Erro - Retornando ao menu")
                        print("-"*36)
                        menu()
    else:
        print("Erro - Retornando ao menu")
        print("-"*36)
        menu()


def sacar():
    os.system('cls')
    global extratoG
    global valor_banco
    print(f"Saldo em banco: {valor_banco}")
    valor_sacar = float(input("Digite o valor que deseja sacar: "))
    if valor_sacar > valor_banco:
        print("O valor exedeu a quantidade em conta! ")
        try:
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
        except:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
        match continuar:
            case 1:
                menu()
                os.system('cls')
            case 2: 
                os.system('cls')
                print("Programa encerrado")
            case _:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
    else:
        confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar saque!\n ")
        if confirmacao == "1":
            valor_banco -= valor_sacar
            extratoG.append(f"Saque no valor de: R$:{valor_sacar}")
            os.system('cls')
            print("Valor Sacado! ")
            try:
                    continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
            except:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
            match continuar:
                case 1:
                    os.system('cls')
                    menu()
                case 2: 
                    os.systemX('cls')
                    print("Programa encerrado")
                case _:
                    print("Erro - Retornando ao menu")
                    print("-"*36)
                    menu()
        elif confirmacao == "2":
            print("Processo interrompido!")
            try:
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
            except:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
            match continuar:
                case 1:
                    os.system('cls')
                    menu()
                case 2: 
                    os.system('cls')
                    print("Programa encerrado")
                case _:
                    print("Erro - Retornando ao menu")
                    print("-"*36)
                    menu()
def investimento():
    try:
        investir = float(input("Quanto deseja investir?\nO valor rende 12% ao ano: "))
    except:
        print("Digite um valor valido! Não deve possuir letras e simbolos!")
        print("-"*36)
        investimento()
    global valor_banco
    if investir <= valor_banco:
        global valor_investido
        valor_banco -= investir
        valor_investido += investir
        os.system('cls')
        print(f"Valor investido!\nValor em processo de investimento: {valor_investido}")
        try:
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
        except:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
        match continuar:
            case 1:
                os.system('cls')
                menu()
            case 2: 
                os.system('cls')
                print("Programa encerrado")
            case _:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
    else: 
        print("O valor exedeu a quantidade em conta! ")
        try:
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
        except:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
        match continuar:
            case 1:
                os.system('cls')
                menu()
            case 2: 
                os.system('cls')
                print("Programa encerrado")
            case _:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()

def status_investimento():
    global mesespassados
    global valor_investido
    global total_investimentos
    total_investimentos = valor_investido * mesespassados * 0.12
    valor_investido += total_investimentos
    print(f"Valor investido: {valor_investido}\nValor Recebido dos investimentos:{total_investimentos}")
    try:
        continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
    except:
        print("Erro - Retornando ao menu")
        print("-"*36)
        menu()
    match continuar:
        case 1:
            os.system('cls')
            menu()
        case 2: 
            os.system('cls')
            print("Programa encerrado")
        case _:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()


def emprestimo():
    os.system('cls')
    global valor_banco
    score = valor_banco*10
    print(f"O seu limite é definito em relação ao valor em banco!\nO seu limite é de:{score}")
    if score <= 0:
        print("Você não valor disponivel para emprestimo")
        try:
            continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
        except:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
        match continuar:
            case 1:
                os.system('cls')
                menu()
            case 2: 
                os.system('cls')
                print("Programa encerrado")
            case _:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
    else:
        valor_emprestimo = float(input("Qual o valor do emprestimo? "))
        try:
            confirmacao = input("Deseja continuar?\n1- Continuar\n2- Cancelar emprestimo!\n ")
        except:
            print("Digite uma opção valida! Não pode conter letras e simbolos!")
        if confirmacao == "1":
            valor_banco += valor_emprestimo
            os.system('cls')
            print("Valor Recebido! ")
            try:
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
            except:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
            match continuar:
                case 1:
                    os.system('cls')
                    menu()
                case 2: 
                    os.system('cls')
                    print("Programa encerrado")
                case _:
                    print("Erro - Retornando ao menu")
                    print("-"*36)
                    menu()
        elif confirmacao == "2":
            print("Processo interrompido!")
            try:
                continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
            except:
                print("Erro - Retornando ao menu")
                print("-"*36)
                menu()
            match continuar:
                case 1:
                    os.system('cls')
                    menu()
                case 2: 
                    os.system('cls')
                    print("Programa encerrado")
                case _:
                    print("Erro - Retornando ao menu")
                    print("-"*36)
                    menu()
def capital():
    os.system('cls')
    global valor_banco
    print(f"Valor em banco: {valor_banco}") 
    try:
        continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
    except:
        print("Erro - Retornando ao menu")
        print("-"*36)
        menu()
    match continuar:
        case 1:
            os.system('cls')
            menu()
        case 2: 
            os.system('cls')
            print("Programa encerrado")
        case _:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()
def finalizar():
    os.system('cls')
    print("Programa encerrado!")

def erro():
    os.system('cls')
    print("Erro - Retornando ao menu")
    print("-"*36)
    menu()

def maquina_tempo():
    global mesespassados
    print("MAQUINA DO TEMPO")
    print("-"*36)
    print("A maquina do tempo passa de 12 em 12 meses por vez! ")
    try:
        continuar = int(input("1 - Passar 12 meses\n2 - Cancelar\n"))
    except:
        print("Digite uma opção valida! Não pode conter numeros e simbolos! ")
        print("-"*36)
        maquina_tempo()
    if continuar == 1:
            mesespassados += 1
    while continuar == 1:
        continuar = int(input("1 - Passar mais 12 meses\n2 - Cancelar\n"))
        os.system('cls')
        if continuar == 1:
            mesespassados += 1 
    os.system('cls')
    print("Retornando ao menu principal!")
    print("-"*36)
    menu()

def extrato ():
    print("== EXTRATO ==:")
    global extratoG
    for deposito in extratoG:
        print(deposito)
    try:
        continuar = int(input("Deseja fazer mais alguma operação?\n1- Menu de Opções\n2- Encerrar programa\n"))
    except:
        print("Erro - Retornando ao menu")
        print("-"*36)
        menu()
    match continuar:
        case 1:
            os.system('cls')
            menu()
        case 2: 
            os.system('cls')
            print("Programa encerrado")
        case _:
            print("Erro - Retornando ao menu")
            print("-"*36)
            menu()

menu()