Idade = int(input("Qual a sua idade? "))
TempoConribuicao = int(input("Qual o seu tempo de contribuição? "))

if Idade >= 65 or TempoConribuicao >= 35:
    print("Você já pode se aposentar!")
else:
    print("Você ainda não pode se aposentar.")