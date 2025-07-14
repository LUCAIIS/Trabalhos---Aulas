entradausuario = input("Digite seu Usuario: ")
entradasenha = input("Digite sua senha: ")
usuario = "admin"
senha = "1234"
if entradausuario == usuario and entradasenha == senha:
    print("A Login bem-sucedido")
if  entradausuario != usuario and entradasenha != senha:
    print("Usuario e Senha invalidos")
if entradasenha != senha:
    print("Senha invalida")
if entradausuario != usuario:
    print("Usuario invalido")



