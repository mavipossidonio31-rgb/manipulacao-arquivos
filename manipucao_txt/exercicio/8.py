def contar_palavras():
    with open("texto.txt", "r") as arquivo:
        texto = arquivo.read()

    palavras = texto.split()

    print("Quantidade de palavras:", len(palavras))


contar_palavras()