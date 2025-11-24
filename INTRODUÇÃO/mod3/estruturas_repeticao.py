texto = input("Digite um texto: ") # Solicita ao usuário que digite um texto
VOGAIS = "AEIOU" # Define as vogais maiúsculas

for letra in texto: # Itera sobre cada letra no texto
    if letra.upper() in VOGAIS: # Verifica se a letra é uma vogal
        print("As encontradas foram:", letra) # Exibe a vogal encontrada
    