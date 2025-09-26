numero1 = int(input("Digite seu primeiro numero =>"))
numero2 = int(input("Digite o seu segundo numero =>"))

if numero1 > numero2:
    print(f"o {numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"o {numero2} é maior que o {numero1}")
else:
    print("os numeros são iguais")
