nota = float(input("Digite sua nota final: "))

if nota >=9:
    print("Aprovado com merito")
elif nota >=7 and nota < 9:
    print("Aprovado")
elif nota >=5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
