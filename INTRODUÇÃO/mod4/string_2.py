nome = "Lucas"
idade = 17
profissao = "Programador"
lingua = "Python"

dados = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": lingua
} # dicionário com os dados

print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" % (nome, idade, profissao, lingua)) # formatação antiga
print("Nome: {} Idade: {} Profissão: {} Linguagem: {}".format(nome, idade, profissao, lingua)) # formatação com .format()

# A linha abaixo exige que os valores estejam na ordem correta e todos sejam passados manualmente.
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {lingua}") # formatação com f-strings


# Usar .format(**dados) é mais prático quando você já tem um dicionário com os dados,
# pois não precisa se preocupar com a ordem dos argumentos e pode adicionar/remover campos facilmente.
# Os nomes entre {} devem ser iguais às chaves do dicionário, assim o método associa cada valor corretamente.
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados)) # formatação com dicionário