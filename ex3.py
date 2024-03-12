ValorCompra = float(input('Digite o valor da compra:'))

desconto = ValorCompra * 0.20
preco_a_pagar = ValorCompra - desconto

if ValorCompra >200:
    print(f"Um desconto de 20% em uma compra de R${ValorCompra:.2f} vale R${desconto:.2f}.")
    print(f"O valor a pagar é de R${preco_a_pagar:.2f}")

else:
    print("Não há desconto pois a compra deu abaixo de R$200")
