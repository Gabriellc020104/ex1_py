valorÁgua= float(input("Digite o valor  da conta de água:"))
valorLuz= float(input("Digite o valor  da conta de Luz:"))
valorTelefone= float(input("Digite o valor  da conta de Telefone:"))
salário = float(input('Digite o valor do seu salário:'))

restoSalário = salário - valorTelefone - valorLuz - valorÁgua

if salário>valorÁgua and valorLuz and valorTelefone:
    print(f' Contas quitadas , seu salário pós o pagamento das contas ficou de : {restoSalário}')
else:
   print("Salário Insuficiente") 