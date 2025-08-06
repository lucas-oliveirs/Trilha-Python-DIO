saldo = 1000 # saldo é 1000
saque = 250 # saque é 250
limite = 200 # limite é 200
conta_especial = True  # conta especial é True

print(True and True)  # Operador lógico AND
print(True or False)  # Operador lógico OR  
print(not False)  # Operador lógico NOT

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # Verifica se o saldo é suficiente para o saque considerando o limite e a conta especial
print(exp)  # Resultado da expressão lógica

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # Verifica se o saldo é suficiente para o saque considerando o limite e a conta especial
print(exp2)  # Resultado da expressão lógica

