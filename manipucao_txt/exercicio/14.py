def gerenciar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arq:
            tarefas = [linha.strip() for linha in arq.readlines()]
    except FileNotFoundError:
        tarefas = []

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nova = input("Digite a nova tarefa: ")
            tarefas.append(nova)
        elif opcao == "2":
            print("\n--- LISTA DE TAREFAS ---")
            for i, t in enumerate(tarefas, 1):
                print(f"{i} - {t}")
        elif opcao == "3":
            num = int(input("Número da tarefa a remover: "))
            if 0 < num <= len(tarefas):
                tarefas.pop(num - 1)
                print("Tarefa removida!")
            else:
                print("Número inválido.")
        elif opcao == "4":
            with open("tarefas.txt", "w", encoding="utf-8") as arq:
                for t in tarefas:
                    arq.write(t + "\n")
            print("Tarefas salvas. Saindo...")
            break
        else:
            print("Opção inválida!")

gerenciar_tarefas()