saldo = 0
periodo = int(input("Digite por quantos meses deseja fazer o investimento: "))
valor = float(input("Digite o valor que deseja investir por mês: "))
juros = float(input("Digite o percentual de Juros: "))
for i in range(periodo):
    juroMes = saldo * juros/100
    saldo += juroMes
    saldo += valor
    print(f"Os Juros do Periodo{i+1}: {juroMes:.2f}")
    print(f"Periodo {i+1}: {saldo:.2f}")