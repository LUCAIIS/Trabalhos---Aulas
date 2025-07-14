operacao = int(input("Qual operaçao deseja fazer (1 – Quadrado, 2 – Retângulo, 3 – Triângulo, 4 – Círculo) "))
match operacao:
    case 1:
        valor =float(input("Qual a altura/base do quadrado? "))
        final = valor * 2
        print(f"A area do quadrado é de {final}m2 ")
    case 2:
        valor = float(input("Digite a base do retangulo: "))
        valor2 = float(input("Digite o valor da altura"))
        final = valor * valor2
        print("A area do retangulo é de {final}")
    case 3:
        valor1 = float(input("Digite o valor da altura do triangulo: "))
        valor2 = float(input("ual o valor da base"))
        final = (valor1 * valor2)/ 2
        print(f"O valor do triangulo é de {final}m2")
    case 4:
        valor1 = float(input("Qual o raio do circulo"))
        m = valor1 * 3.14
        print(f"A area aproximada é de {m}m2")