contatos = {
    "Alice": {"telefone": "1234-5678", "email": "alice"}, # a chave é "Alice" e o valor é outro dicionário
    "Bob": {"telefone": "8765-4321", "email": "bob"} # a chave é "Bob" e o valor é outro dicionário
} # dicionário aninhado, que é um dicionário dentro de outro dicionário

copia = contatos.copy()  # cria uma cópia rasa do dicionário contatos
copia["Alice"]["email"] = "alice_novo"  # modifica o email de Alice na cópia

#
#
#
dict.fromkeys(["chave1", "chave2"], "valor padrão")  # cria um dicionário com chaves padrão

#
#
#

contatos.get("Alice")  # acessa o valor associado à chave "Alice"
contatos.get("Carlos", {"telefone": "0000-0000", "email": "desconhecido"})  # retorna valor padrão se a chave não existir

contatos.items()  # retorna uma visão dos pares chave-valor do dicionário contatos

contatos.keys()  # retorna uma visão das chaves do dicionário contatos

contatos.pop("Bob")  # remove o par chave-valor associado à chave "Bob"
contatos.pop("Carlos", {"telefone": "0000-0000", "email": "desconhecido"})  # retorna valor padrão se a chave não existir

contatos.setdefault("David", {"telefone": "1111-2222", "email": "david"})  # adiciona um novo par chave-valor se a chave não existir, no caso "David"

contatos.update({"Alice": {"telefone": "9999-8888", "email": "alice_atualizado"}})  # atualiza o valor associado à chave "Alice"