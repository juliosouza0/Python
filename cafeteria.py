import os
import time

def Pagamento(pagamento, controlador):
    if pagamento == 1 or pagamento == 2 or pagamento == 3:
        print("\nPagamento realizado com sucesso!")
    else:
        print("\nVc não pode sair sem pagar!")

def SomarValor(escolha):
    if escolha == 1:
        SomaValor = SomaValor + 2.00
    elif escolha == 2:
        SomaValor = SomaValor + 3.00
    elif escolha == 3:
        SomaValor = SomaValor + 5.00
    elif escolha == 4:
        SomaValor = SomaValor + 0.00
    elif escolha == 0:
        controlador = 0
        print ("\nCaixa Fechado!")
        SomarValor(escolha)
        pagamento = int(input ("\nQual a forma de pagamento?\n1 - Cartão de crédito ou débito\n2 - Pix\n3 - Dinheiro\n"))
        Pagamento(pagamento)
    print ("\nValor total do pedido: R$", SomaValor)



controlador = None
SomaValor = 0
pedido = ""
SomaCafe = 0
SomaCappuccino = 0
SomaBolo = 0

while controlador != 0:
    print ("\n------------------------------")
    print ("----------Cafeteria-----------")
    print ("------------------------------\n")
    print ("1 - Café - R$2,00")
    print ("2 - Cappuccino - R$3,00")
    print ("3 - Bolo de Chocolate - R$5,00")
    print ("0 - Fechar Caixa")
    escolha = int(input("Escolha um produto: "))
    
    if escolha == 1:
        SomaValor = SomaValor + 2.00
        SomaCafe = SomaCafe + 1
        pedido = pedido + "\nCafé"
        time.sleep(2)
        os.system('cls')
    elif escolha == 2:
        SomaValor = SomaValor + 3.00
        SomaCappuccino = SomaCappuccino + 1
        pedido = pedido + "\nCappuccino"
        time.sleep(2)
        os.system('cls')
    elif escolha == 3:
        SomaValor = SomaValor + 5.00
        SomaBolo = SomaBolo + 1
        pedido = pedido + "\nBolo de Chocolate"
        time.sleep(2)
        os.system('cls')
    elif escolha == 0:
        controlador = 0
        print ("\nCaixa Fechado!")
        SomarValor(escolha)
        pagamento = int(input ("\nQual a forma de pagamento?\n1 - Cartão de crédito ou débito\n2 - Pix\n3 - Dinheiro\n"))
        Pagamento(pagamento)
    else:
        print ("\nOpção invalida, tente novamente!")
        time.sleep(2)
        os.system('cls')
    print (f"\nTotal do pedido: Café: {SomaCafe} unidades\nCappuccino: {SomaCappuccino} unidades\nBolo de chocolate: {SomaBolo} unidades")