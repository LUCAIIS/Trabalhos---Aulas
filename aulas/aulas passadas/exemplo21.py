#esse é o exerccio 11
senha = input("Digite a sua senha: ")
temespecial = ("@" in senha or "#" in senha 
                or "*" in senha or "!"in senha
                or "%" in senha or "$"in senha
                or "&"in senha)
temnumeros =  ("1" in senha or "2" in senha 
                or "3"in senha or "4"in senha
                or "5"in senha or "6"in senha
                or "7"in senha or "8"in senha 
                or "9"in senha or "0"in senha)
temmaiusculas = ("A" in senha or "B" in senha 
                or "C"in senha or "D"in senha
                or "E"in senha or "F"in senha
                or "G"in senha or "H"in senha 
                or "I"in senha or "J"in senha
                or "K"in senha or "L"in senha 
                or "M"in senha or "N"in senha
                or "O"in senha or "P"in senha
                or "Q"in senha or "R"in senha 
                or "S"in senha or "T"in senha) # nao vou colocar todas as letras
tamanho = (len(senha)>= 8)
if temespecial and temnumeros and  temmaiusculas:
    print(f"A senha {senha} é forte o sulficiente")
else:
    print("Senha fraca pelos seguintes motivos: ")
    if not temespecial:
        print("-Deve ter caractere especial")
    if not temnumeros:
        print("-Deve ter pelo menos um numeor")
    if not temmaiusculas:
        print("-Deve ter letra Maiusculas")
    if not tamanho:
        print("-Deve ter pelo menos 8 caracteres")