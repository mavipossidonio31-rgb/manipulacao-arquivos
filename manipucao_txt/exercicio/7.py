def buscar_nome():
    nomes = []

    with open("nomes.txt", "r") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            nomes.append(nome)

    nome_pesquisa = input("Digite o nome: ")

    if nome_pesquisa in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


buscar_nome()