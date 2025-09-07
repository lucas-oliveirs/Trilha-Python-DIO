def criar_carro(*modelo, ano, placa, marca, motor, combustivel): # Todos os parâmetros devem ser nomeados
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Onix", ano=2022, placa="XYZ-9876", marca="Chevrolet", motor=1.4, combustivel="Gasolina") # Todos os argumentos por nome