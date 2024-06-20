menu = """

    ========= BANCO LUISA DO BRASIL =========
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair
    =========================================

=> """

saldo = 0
limite_valor = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado de R$ {valor:.2f} com sucesso!\n")
        else:
            print(f"Operação não realizada! O valor informado é inválido. Por favor, tente novamente.")

    elif opcao == "1":
        valor = float(input("Informe o valor que deseja sacar: "))
        
        saldo_insuficiente = saldo < valor
        excedeu_limite = valor > limite_valor
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação não realizada, pois não há saldo suficiente.\n")
        
        elif excedeu_limite:
            print(f"Operação não realizada, pois o  valor de R$ {valor:.2f} ultrapassa o limite de R$ {limite_valor:.2f}.\n")

        elif excedeu_saques:
            print("Operação não realizada, pois excedeu o número de saques diários. Por favor, tente novamente amanhã.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso, por favor retire o seu dinheiro!\n")

        else:
            print(f"Operação não realizada! O valor informado é inválido. Por favor, tente novamente.")

    elif opcao == "2":
        print("\n================ EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("========================================")
    
    elif opcao == "3":
        print("Obrigada por ser nosso(a) cliente. Tenha um bom dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")







    
