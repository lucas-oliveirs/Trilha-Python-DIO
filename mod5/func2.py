# Este código define duas funções:
# 1. calcular_total: recebe uma lista de números e retorna a soma deles.
# 2. retorna_antecessor_e_sucessor: recebe um número e retorna uma tupla com seu antecessor e sucessor.
# Depois, o código chama essas funções e imprime os resultados.

# Em Python, uma tupla é uma estrutura de dados que armazena múltiplos valores em uma única variável.
# Ela é semelhante a uma lista, mas é imutável (não pode ser alterada após a criação).
# Exemplo: tupla = (1, 2, 3)
# Tupla é uma coleção ordenada de elementos, semelhante a uma lista, porém imutável.
# Ou seja, após criada, seus valores não podem ser alterados, adicionados ou removidos.
# É útil para armazenar dados que não devem ser modificados.

def calcular_total(numeros): # Função que calcula a soma de uma lista de números
    return sum(numeros) # Retorna a soma dos números da lista

def retorna_antecessor_e_sucessor(numero): # Função que retorna o antecessor e sucessor de um número
    antecessor = numero - 1 # Calcula o antecessor
    sucessor = numero + 1   # Calcula o sucessor

    return antecessor, sucessor # Retorna uma tupla com o antecessor e sucessor

def function_example(): # Exemplo de função adicional
    print("This is an example function.") # Apenas imprime uma mensagem
    # Não possui return, então retorna None por padrão.

print(calcular_total([10, 20, 30, 40, 50])) # Chama a função calcular_total passando uma lista de números.
# O resultado será a soma dos valores da lista, ou seja, 150.

print(retorna_antecessor_e_sucessor(10)) # Chama a função retorna_antecessor_e_sucessor passando o número 10.
# O resultado será uma tupla com o antecessor e sucessor: (9, 11).

print(function_example()) # Retorna none porque a função não possui return explícito.