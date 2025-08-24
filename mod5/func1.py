def exibir_mensagem(): # Sem parâmetro
    print("Olá mundo!") # Sem argumento

def exibir_mensagem2(nome): # Parâmetro obrigatório
    print(f"Seja bem-vindo(a) {nome}") # Argumento

def exibir_mensagem3(nome = "Usuário"): # Parâmetro opcional
    print(f"Seja bem-vindo(a) {nome}") # Argumento

exibir_mensagem() # Chamada da função
exibir_mensagem2(nome="Bola de Neve") # Argumento nome
exibir_mensagem3() # Sem argumento, usa o padrão
exibir_mensagem3(nome="Maria") # Com argumento, substitui o padrão