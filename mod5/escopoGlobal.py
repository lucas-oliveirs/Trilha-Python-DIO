salario = 2000

def salario_bonus(bonus):
    global salario # Indica que a variável salario é global
    salario += bonus # Adiciona o bônus ao salário global
    return salario

print(salario_bonus(500)) # Chama a função com um bônus de 500 e imprime o novo salário