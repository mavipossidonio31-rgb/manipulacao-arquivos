def mostrar_numeros():
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())

            if numero % 2 == 0:
                print(numero)


mostrar_numeros()