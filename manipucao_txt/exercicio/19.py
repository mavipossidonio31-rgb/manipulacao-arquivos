def gerar_relatorio():

    vendas = []

    with open("vendas.txt", "r") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            venda = {
                "vendedor": dados[0],
                "produto": dados[1],
                "valor": float(dados[2])
            }

            vendas.append(venda)

    total = 0

    print("===== VENDAS =====")

    for venda in vendas:

        print(
            venda["vendedor"],
            "-",
            venda["produto"],
            "- R$",
            venda["valor"]
        )

        total = total + venda["valor"]

    print()
    print("TOTAL DE VENDAS: R$", total)


gerar_relatorio()