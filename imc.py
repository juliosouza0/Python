nome = input("Digite seu nome: ")
anonascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - anonascimento
peso = float(input("Digite seu Peso (em Kg): "))
altura = float(input("Digite sua altura (Ex: 1.70): "))
imc = peso / (altura*altura)
classificacao = ""

if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc >= 18.5 and imc < 24.9:
    classificacao = "peso normal"
elif imc >= 25 and imc < 29.9:
    classificacao = "sobrepeso"
elif imc >= 30 and imc < 34.9:
    classificacao = "obesidade grau 1"
elif imc >= 35 and imc < 39.9:
    classificacao = "obesidade grau 2"
else:
    classificacao = "obesidade grau 3"

print (f"Olá {nome}, você tem {idade} anos e seu imc é igual a: {imc:.2f}, e segundo a tabela de classificação da OMS você está com {classificacao}")
print (f"Nome: {nome}; Idade: {idade} anos; IMC: {imc:.2f}; Classificação: {classificacao}")
