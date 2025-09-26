usuario = str(input("Digite o usuario:"))
senha = int(input("Digite a senha"))

if usuario != "admin":  
    print("Acesso negado")
elif senha != 1234:
    print("acesso negado")  
else:
    print("Acesso permitido")

    

