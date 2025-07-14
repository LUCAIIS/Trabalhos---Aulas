total_pessoas = float(input("Quantas pessoas estão na mesma comnada? "))
divida = float(input("Quanto foi o valor da conta? "))
valortaxa = divida * 0.10
dividataxa = divida + valortaxa
print("lembrando que o valor total é somado a mais 10% (taxa de serviço)")
print('valor da taxa', valortaxa)
print("Valor sem a taxa: ", divida,"Reais")
print("Valor com a taxa: ", dividataxa, "Reais")
valorcada = dividataxa/total_pessoas
Valorcadasemtaxa = divida/total_pessoas
print("Cada um deve pagar(sem taxa): ", Valorcadasemtaxa)
print("Cada um deve pagar(com a taxa): ", valorcada)