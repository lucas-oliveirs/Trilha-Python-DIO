refresh = -1 # Variável para controle do loop
print("Bem-vindo ao sistema de saque!") # Mensagem de boas-vindas

while refresh !=0: # Inicia o loop enquanto refresh não for 0
    print("Iniciando o processo de saque...") # Mensagem de início do processo
    saldo = 2000 # Exemplo de saldo inicial
    saque = float(input("Digite o valor você deseja sacar: ")) # Solicita ao usuário o valor do saque

    if saque <= saldo: # Verifica se o saldo é suficiente para o saque
        print("Saque realizado com sucesso!")
        
    else:
        print("Saldo insuficiente para realizar o saque.")

    opcao = int(input("Digite 1 para continuar ou 2 para sair: ")) # Solicita ao usuário uma opção

    if opcao == 1: # Verifica se a opção é 1
        print("Você escolheu continuar.")

    elif opcao == 2: # Verifica se a opção é 2
        print("Você escolheu sair.")

    else:
        print("Opção inválida.")

    # Estrutura condicional ternária para definir o status da operação
    status = "Sucesso" if saldo > saque else "falha" # Define o status com base no saldo
    print(f"O status da operação é: {status}") # Exibe o status da conta

    for numero in range(0, 51, 5): # Loop para imprimir números de 0 a 50 com passo de 5
        print(numero) # Exibe os números de 0 a 50 com passo de 5

    for num in range(100): # Loop para verificar números de 0 a 99
        if num == 50: # Verifica se o número é 50
            print("Número 50 encontrado, encerrando o loop.") # Encerra o loop se o número for 50
            break # Encerra o loop

    for number in range(100): # Loop para imprimir números de 0 a 99
        if number == 12: # Verifica se o número é 12
            continue # Pula o número 12

    refresh = int(input("Digite 0 para encerrar o programa ou qualquer outro número para continuar: ")) # Solicita ao usuário uma ação para a continuação do loop
    if refresh == 0:
        print("Programa encerrado.")