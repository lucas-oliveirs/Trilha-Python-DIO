def somar(a, b):# Função que soma dois números
    return a + b # Retorna a soma dos dois números

def exibir_resultado(a, b, funcao): # Recebe dois números e uma função como argumentos
    resultado = funcao(a, b) # Chama a função passada como argumento
    print(f"O resultado da operação é: {resultado}") # Formatação com f-strings

exibir_resultado(10, 20, somar) # Passa a função somar como argumento