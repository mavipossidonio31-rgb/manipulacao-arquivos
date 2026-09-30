def sistema_alunos():

    alunos = []

    # Ler os alunos do arquivo
    try:

        with open("alunos.txt", "r") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                aluno = {
                    "id": int(dados[0]),
                    "nome": dados[1],
                    "idade": int(dados[2]),
                    "curso": dados[3]
                }

                alunos.append(aluno)

    except:

        pass

    while True:

        print()
        print("===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        # LISTAR
        if opcao == "1":

            print()
            print("===== ALUNOS =====")

            for aluno in alunos:

                print(
                    aluno["id"],
                    "-",
                    aluno["nome"],
                    "-",
                    aluno["idade"],
                    "anos"
                )

        # BUSCAR
        elif opcao == "2":

            id_pesquisa = int(input("Digite o ID: "))

            encontrado = False

            for aluno in alunos:

                if aluno["id"] == id_pesquisa:

                    print()
                    print("Aluno encontrado:")
                    print("Nome:", aluno["nome"])
                    print("Idade:", aluno["idade"])
                    print("Curso:", aluno["curso"])

                    encontrado = True

            if encontrado == False:

                print("Aluno não encontrado!")

        # CADASTRAR
        elif opcao == "3":

            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            novo_id = len(alunos) + 1

            aluno = {
                "id": novo_id,
                "nome": nome,
                "idade": idade,
                "curso": curso
            }

            alunos.append(aluno)

            with open("alunos.txt", "w") as arquivo:

                for aluno in alunos:

                    arquivo.write(
                        str(aluno["id"]) + ";" +
                        aluno["nome"] + ";" +
                        str(aluno["idade"]) + ";" +
                        aluno["curso"] + "\n"
                    )

            print("Aluno cadastrado com sucesso!")

        # REMOVER
        elif opcao == "4":

            id_remover = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:

                if aluno["id"] == id_remover:

                    alunos.remove(aluno)
                    encontrado = True
                    break

            if encontrado:

                with open("alunos.txt", "w") as arquivo:

                    for aluno in alunos:

                        arquivo.write(
                            str(aluno["id"]) + ";" +
                            aluno["nome"] + ";" +
                            str(aluno["idade"]) + ";" +
                            aluno["curso"] + "\n"
                        )

                print("Aluno removido!")

            else:

                print("Aluno não encontrado!")

        # ALTERAR
        elif opcao == "5":

            id_alterar = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:

                if aluno["id"] == id_alterar:

                    aluno["nome"] = input("Novo nome: ")
                    aluno["idade"] = int(input("Nova idade: "))
                    aluno["curso"] = input("Novo curso: ")

                    encontrado = True

            if encontrado:

                with open("alunos.txt", "w") as arquivo:

                    for aluno in alunos:

                        arquivo.write(
                            str(aluno["id"]) + ";" +
                            aluno["nome"] + ";" +
                            str(aluno["idade"]) + ";" +
                            aluno["curso"] + "\n"
                        )

                print("Aluno alterado!")

            else:

                print("Aluno não encontrado!")

        # SAIR
        elif opcao == "6":

            print("Programa encerrado.")
            break

        else:

            print("Opção inválida!")


sistema_alunos()