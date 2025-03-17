velocidade = int(input("Qual a velocidade do veículo? "))

if velocidade > 120:
    print("multa grave")
elif velocidade > 80 and velocidade <= 120:
    print("velocidade acima do permitido")
else:
    print("velocidade dentro do limite") 
    