
turno = input("Digite o turno de trabalho (N para noturno, D para diurno): ")
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))


if turno.upper() == 'N':
    valor_hora = 45.00
else:
    valor_hora = 37.50


salario = horas_trabalhadas * valor_hora


print(f"O valor do salário é R${salario:.2f}")