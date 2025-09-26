valor = float(input("Digite o valor do produto \n"))

desconto = valor * 0.1
promoção = valor - desconto

if valor > 100:
    print(f'o produto está em promoção novo valor: {promoção}')
else:
    print(f'preço: {valor}')
