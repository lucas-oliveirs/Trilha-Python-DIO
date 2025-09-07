def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # Barra após os três primeiros parâmetros
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Ka", 2020, "ABC-1234", marca="Ford", motor=1.0, combustivel="Flex") # argumentos por posição e nomeados

criar_carro(modelo="Ka", ano=2020, placa="ABC-1234", marca="Ford", motor=1.0, combustivel="Flex") # forma incorreta, a função exige os três primeiros argumentos por posição e o restante pode ser por nome ou posição