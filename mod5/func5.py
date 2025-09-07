def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # Barra após os três primeiros parâmetros
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro("Ka", 2020, "ABC-1234", "Ford", 1.0, "Flex") # Todos os argumentos por posição



def criar_carro_kw(*, modelo, ano, placa, marca, motor, combustivel): # Todos os parâmetros devem ser nomeados
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro_kw(modelo="Onix", ano=2022, placa="XYZ-9876", marca="Chevrolet", motor=1.4, combustivel="Gasolina") # Todos os argumentos por nome



def criar_carro_hibrido(modelo, ano, /, placa, *, marca, motor, combustivel): # Híbrido: posição, posição/nome, nomeados
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro_hibrido("Fiesta", 2018, "DEF-4567", marca="Ford", motor=1.6, combustivel="Gasolina") # modelo e ano por posição, placa por posição ou nome, demais por nome