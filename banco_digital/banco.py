""""Descrição do Projeto: Sistema Bancário com Python

Este projeto desenvolve um sistema bancário simples em Python, permitindo operações básicas como:

Depósito: O usuário pode adicionar valores à conta, com validação para valores positivos e registro no extrato.
Saque: Respeita o limite diário de saques e saldo disponível, com validações.
Extrato: Exibe todas as transações e o saldo final.
O sistema é interativo, com menu de opções e controle contínuo das operações, garantindo entradas válidas e respeito às regras definidas. """

# criação Menu
menu = """
    #### MENU ####
    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [q] Sair  
    ESCOLHA UMA OPÇÂO :
"""
# declaração das variavel
salde = 0.00
Extrato = "" 
limite_saque = 3

# laço while para iterar nosso Menu
while True: 

    opcao = input(menu) #criação da variavel opção que imprima nosso Menu na tela

    # criando bloco depositar 
    if opcao == "d": 
        valor = float(input("Digitge o valor a Depositar: "))
        if valor <= 0 :
            while valor <= 0:
                print("valor digitado não existe")
                valor = float(input("Digitge o valor a Depositar: "))
        salde += valor
        Extrato += f"Depositadao {valor: .2f}\n"
        print(f"Seu saldo é {salde: .2f}")
    
    #criando bloco sacar
    elif opcao == "s":
        valor = float(input("Digite o valor a Sacar: "))
        if valor <= 0:
            while valor <= 0:
                print("valor digitado não existe")
                valor = float(input("Digite o valor a Sacar: "))
        if valor > 500 :
            print("Não pode efetuar o saque deste valor o Limite Diario é 500")
        elif limite_saque > 0 and salde >= valor:
            salde -= valor
            Extrato += f"Sacar {valor: .2f}\n"
            limite_saque -=1
            print(f"Seu saldo é {salde: .2f}")
        elif valor > salde and limite_saque:
            print("salde insuficiente")
        else:
            print("Limite de saque por dia e 3")

    #criando bloco extrato
    elif opcao == "e":
        print(f"#####EXTRATO#####:\n{Extrato}")
        print(f"solde final: {salde: .2f}")

    #criando bloco extrato 
    elif opcao == "q":
         print("Saindo do sistema.")
         print("***Obrigado Por escolher Nosso Sistema!!!***")
         break
    #criando bloco caso usuario digitou opção errada
    else:
        print("opcão não existe ")  # saida