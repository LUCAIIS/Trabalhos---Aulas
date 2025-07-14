idade=int(input("Qual a sua idade? "))
if idade <= 12:
    print("criança")
elif idade <=17:
    print("adolecent")
elif idade <=59:
    print("adulto")
else:
    print("idoso")