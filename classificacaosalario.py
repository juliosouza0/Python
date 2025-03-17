salario = float(input("Digite seu salario: "))

if salario < 2000:
    print("Renda Baixa")
elif salario >= 2000 and salario <= 5000:
    print("Renda Média")
else:
    print("Renda Alta")