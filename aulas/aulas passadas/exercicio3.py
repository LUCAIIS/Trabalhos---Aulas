valor = float(input("Digite o valor vendido no mês: "))
categoria = input("Qual a sua categoria? Digite 1 para iniciante, Digite 2 para experiente, ou Digite 3 Para Senior")
iniciante = ("1" in categoria)
experiente = ("2" in categoria)
senior = ("3" in categoria)
premio = 500
bonus = valor >= 10000
if iniciante:
    porcentagem = 0.05
    comissao = valor * porcentagem
    print(f"A comissão é de {comissao}R$ ")
elif experiente:
    porcentagem = 0.10
    comissao = valor * porcentagem
    print(f"A comissão é de {comissao}R$ ")
elif senior:
    porcentagem = 0.15
    comissao = valor * porcentagem
    print(f"A comissão é de {comissao}R$ ")
if bonus:
    premiototal = comissao + premio
    print(f"Voce recebeu um premio de R${premio}")
    print(f"O valor total foi de R${premiototal}")
else:
    print(f"O valor a ser recebido é de R${comissao}")
