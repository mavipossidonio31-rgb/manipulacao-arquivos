def calcular_estoque():

    produtos = []

    with open("produtos.txt", "r") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            produto = {
                "nome": dados[0],
                "preco": float(dados[1]),
                "quantidade": int(dados[2])
            }

            produtos.append(produto)

    total = 0

    for produto in produtos:

        valor = produto["preco"] * produto["quantidade"]

        total = total + valor

    print("Valor total do estoque: R$", total)


calcular_estoque()