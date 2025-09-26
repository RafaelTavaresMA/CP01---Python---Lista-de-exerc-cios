nota = float(input("Digite sua nota \n"))


if nota < 0 or nota > 10:
    print("Essa nota não existe ;-;")
elif nota >= 6:
    print("Você foi aprovado :)")
else:
    print("Você foi reprovado :(")