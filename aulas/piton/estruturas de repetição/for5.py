tempgeral = 0
maior = -100
menor = 100
dias = ["Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sabado"]
for dia in dias:
    temperatura = float(input(f"Temperatura {dia}: "))
    tempgeral+= temperatura
    if temperatura > maior:
        maior = temperatura
        quente = dia
    if temperatura < menor:
        menor = temperatura
        frio = dia
mediatemp = tempgeral / 7
print(f"A Maior temperatura foi: {maior}, no(a) {quente}. ")
print(f"A Menor temperatura foi: {menor}, no(a) {frio}. ")
print(f"A Media da semana foi:{mediatemp:.2f} C. ")
