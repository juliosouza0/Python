usuario = str(input("Digite o nome de usuario: "))
senha = str(input("Digite a senha: "))

if senha != "1234":
    print("Senha invalida")
if usuario != "admin":
    print("Usuario invalido")
if usuario != "admin" and senha != "1234":
    print("Você não pode acessar o login")
else:
    print("Sucesso")