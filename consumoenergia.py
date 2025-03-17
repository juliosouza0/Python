consumo = int(input("Digite o valor do consumo em kWh: "))

if consumo < 100:
    print("Baixo consumo")
elif consumo >= 100 and consumo <= 500:
    print("Consumo médio")
else: 
    print("Consumo alto")