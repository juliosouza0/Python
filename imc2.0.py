def Classificacao(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def Dados(nome, idade, imc, classificacao):
    print(f"Nome: {nome}; Idade: {idade}; IMC: {imc:.2f}; Classificação: {classificacao}")

# Entrada de dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - ano_nascimento
peso = float(input("Digite seu Peso (em Kg): "))
altura = float(input("Digite sua altura (Ex: 1.70): "))

# Cálculo do IMC
imc = peso / (altura * altura)

# Classificacao do IMC
classificacao = Classificacao(imc)

# Exibe os dados
Dados(nome, idade, imc, classificacao)
