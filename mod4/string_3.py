nome = "Lucas"

mensagem = f""" 
    Olá, {nome}. Seja bem-vindo!
Eu espero que você aproveite o curso de Python.
    Qualquer dúvida, é só perguntar.
""" # string multilinha com f-strings, mantendo a formatação original

print(mensagem)

print("""
      ==========================MENU==========================
      |   Opção 1 - Depositar                                |
      |   Opção 2 - Sacar                                    |
      |   Opção 3 - Sair                                     |
      ========================================================
      """) # string multilinha sem f-strings, mantendo a formatação original