temperatura = float(input("Digite a temperatura em C°"))

if temperatura < 0:
    print("Congelante")
elif temperatura >= 0 and temperatura <= 30:
    print("Agradável")
else:
    print("Quente")

