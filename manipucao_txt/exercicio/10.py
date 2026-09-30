def separar_numeros(nome_arquivo):
    pares = []
    impares = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            num = int(linha.strip())
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)

    print("Números pares:")
    print(pares)
    print("\nNúmeros ímpares:")
    print(impares)

separar_numeros("numeros.txt")