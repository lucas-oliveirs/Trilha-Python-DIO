def salvar_carro(marca, modelo, ano, placa): # Define a função salvar_carro com parâmetros obrigatórios
    # salvar o carro no banco de dados
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}") # Imprime os dados do carro salvo

salvar_carro("Ford", "Ka", 2020, "ABC-1234") # Chama a função salvar_carro com argumentos posicionais
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2021, placa="DEF-5678") # Chama a função salvar_carro com argumentos nomeados
salvar_carro(**{"marca": "Fiat", "modelo": "Mobi", "ano": 2019, "placa": "GHI-9012"}) # Chama a função salvar_carro desempacotando um dicionário