pessoa = {"nome": "Ana", "idade": 28, "cidade": "São Paulo"} # dicionário literal

pessoa = dict(nome="Ana", idade=28, cidade="São Paulo") # dicionário usando a função dict()

pessoa["cidade"] = "Rio de Janeiro" # atualizando o valor da chave "cidade"

pessoa["profissão"] = "Engenheira" # adicionando uma nova chave-valor

#
#
#

dados = { "nome": "Carlos", "idade": 35, "cidade": "Belo Horizonte"}

dados["nome"] # acessando o valor da chave "nome"
dados["idade"] # acessando o valor da chave "idade"

#
#
#

contatos = {
    "Alice": {"telefone": "1234-5678", "email": "alice@email.com"},
    "Bob": {"telefone": "8765-4321", "email": "bob@email.com"}
}  # dicionário aninhado

contatos["Alice"]["email"] # acessando o email de Alice
contatos["Bob"]["telefone"] # acessando o telefone de Bob

#
#
#

for chave in contatos:
    print(chave)  # imprime as chaves do dicionário contatos

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")  # imprime chave e valor do dicionário pessoa

print(pessoa)