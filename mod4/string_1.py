nome = "LoUqUetA" # string

print(nome.upper()) # transforma em maiúsculo
print(nome.lower()) # transforma em minúsculo
print(nome.title()) # transforma a primeira letra de cada palavra em maiúsculo

texto = "   Olá, Mundo!   " # string com espaços no início e no fim
print(texto) # imprime a string com espaços
print(texto.strip() + ".") # remove os espaços no início e no fim
print(texto.rstrip() + ".") # remove os espaços à direita
print(texto.lstrip() + ".") # remove os espaços à esquerda

menu = "Python"
print(menu.center(14, "#")) # centraliza a string em um campo de 20 caracteres, preenchendo com '#'
print("-".join(menu)) # insere '-' entre cada caractere da string

for letra in menu: # itera sobre cada caractere da string
    print(letra, end="-") # imprime cada caractere seguido de um espaço
print() # apenas para pular uma linha no final