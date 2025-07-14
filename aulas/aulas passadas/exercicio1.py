turno = input("Qual o seu turno? Digite a letra M para Matutino, a letra V para Vespertino ou a letra N para Noturno ")
matutino = ("M" in turno or "m" in turno)
vespertino =("V" in turno or "v" in turno)
noturno = ("N" in turno or "n" in turno)

if matutino:
    print("Muito Bom Dia!")
elif vespertino:
    print("Muito Boa Tarde!")
elif noturno:
    print("Muito Boa Noite!")
else:
    print("Turno invalido")