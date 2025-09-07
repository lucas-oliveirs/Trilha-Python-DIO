# Função exibir_poema:
# Recebe uma data (ou título), vários versos do poema (*args) e metadados como autor e ano (**dicionario).
# Junta os versos em uma única string, formata os metadados e exibe tudo organizado.

def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista) # Junta os versos do poema, cada um em uma linha.
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()]) # Formata os metadados.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # Monta a mensagem final.
    print(mensagem) # Exibe o poema formatado.

# Exemplo de uso da função:
# Passa o título, dois versos e os metadados autor e ano.
exibir_poema("Seg, 25 de Agosto de 2025", "Zen of Python", "Beautiful is better than ugly.", "Explicit is better than implicit.", autor="Tim Peters", ano=1999)