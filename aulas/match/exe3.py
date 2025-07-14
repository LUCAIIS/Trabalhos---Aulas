operacao = input("Digite um agente de operação (+ Soma, – Subtração, * Multiplicação, / Divisão)")
numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite um numero"))
match operacao:
    case '+':
       total = numero1 + numero2
       print(f"O valor total é de{total}")
    case '-':
       total = numero1 - numero2
       print(f"O valor total é de{total}")
    case '/':
       total = numero1 / numero2
       print(f"O valor total é de{total}")
    case '*':
       total = numero1 * numero2
       print(f"O valor total é de{total}")
    case _:
      print("Operção invalida")