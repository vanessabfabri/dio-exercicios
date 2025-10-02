menu = """ 

[d] Depositar 
[s] Sacar 
[e] Extrato 
[q] Sair 
 
""" 

saldo = 0 
limite = 500 
extrato = [] 
numero_saques = 0 

while True: 
 
    opcao = input(menu) 

    if opcao == "d": 
        deposito = float(input("Depósito - Digite o valor desejado: ")) 
        if deposito > 0: 
            saldo += deposito 
            extrato.append(f"Depósito: R$ {deposito:.2f}") 
        else: 
            print("Valor inválido para depósito.") 

    elif opcao == "s": 
        saque = float(input("Saque - Digite o valor desejado: ")) 
        if saque <= 0: 
            print("Valor inválido para saque.") 
        elif saque > saldo: 
            print("Saldo insuficiente.") 
        elif saque > limite: 
            print("Limite de R$500,00 por saque excedido.") 
        elif numero_saques >= 3: 
            print("Limite de 3 saques diários excedido.") 
        else: 
            numero_saques += 1 
            saldo -= saque 
            extrato.append(f"Saque: R$ {saque:.2f}") 

    elif opcao == "e": 
        if not extrato: 
            print("Não foram realizadas movimentações.") 
        else: 
            print("\nExtrato: ") 
            for mov in extrato: 
                print(mov) 
            print(f"Saldo atual: R${saldo:.2f}.\n") 

    elif opcao == "q": 
        print("Saindo... Obrigado por usar nosso banco!") 
        break 

    else: 
        print("Operação inválida, selecione novamente a operação desejada.") 
