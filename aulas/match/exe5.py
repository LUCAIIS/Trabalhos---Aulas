valor = float(input("Digite o valior em Reais"))
operacao = int(input("Selecione qual operacao deseja fazer (1 – Dólar, 2 – Euro, 3 – Iene)"))
match operacao:
    case 1:
        final = valor / 5.68
        print(f"O valor em dolares sera de {final}$")
    case 2:
        final = valor / 6.37
        print(f"O valor em Euros será de {final}€")
    case 3:
        final = valor * 25,58
        print(f"O valor em Ienes será de {final}")