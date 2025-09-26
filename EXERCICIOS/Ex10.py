numero1 = float(input("Digite o primeiro numero"))
numero2 = float(input("Digite o segundo numero"))
operacao = input("Digite a operação")



if operacao == "+":
    print("resultado:", numero1 + numero2)
elif operacao == "*":
    print("resultado:", numero1 * numero2)
elif operacao == "-":
    print("resultado:", numero1 - numero2)
elif operacao == "/":
    print("resultado:", numero1 / numero2)  
else:
    print("operacao invalida")
  