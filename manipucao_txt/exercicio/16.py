def buscar_produto():

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

    pesquisa = input("Digite o produto: ")

    encontrado = False

    for produto in produtos:

        if produto["nome"].lower() == pesquisa.lower():

            print("Produto encontrado!")
            print("Nome:", produto["nome"])
            print("Preço: R$", produto["preco"])
            print("Quantidade:", produto["quantidade"])

            encontrado = True

    if encontrado == False:
        print("Produto não encontrado!")


buscar_produto()