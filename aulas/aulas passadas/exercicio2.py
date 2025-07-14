meta = float(input("Digite a meta mensal: "))
quinzena1 = float(input("Digite a quantidade produzida na primeira quinzena: "))
quinzena2 = float(input("Digite a quantidade produzida na segunda quinzena: "))
bruto = quinzena1 + quinzena2
tudo = bruto/ meta
porcento = tudo*100
print(f"A porcentagem foi de {porcento}% em relaçao a meta:{meta}")
if porcento >= 100:
    print("Parabéns: Meta atingida!")
elif porcento >= 80 and porcento <= 99.99:
    print("Atenção: produção abaixo da meta.")
elif porcento <= 80:
    print("Meta não atingida.")
else:
    print("Dados Invalidos! ")