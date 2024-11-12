import adoptersController
import animalsController
import shelterController
import databaseUtils
import adoptionsController
import os

personalidades_opcoes = {
    1: "Brincalhão",
    2: "Calmo",
    3: "Curioso",
    4: "Protetor",
    5: "Afetuoso",
    6: "Independente",
    7: "Aventureiro",
    8: "Inteligente"
}

def limpa_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def selecionar_personalidade():
    print("\nSelecione a personalidade:")
    for numero, descricao in personalidades_opcoes.items():
        print(f"{numero} - {descricao}")
    while True:
        escolha = int(input("Digite o número correspondente à personalidade: "))

        if escolha in personalidades_opcoes:
            return personalidades_opcoes[escolha]
        else:
            print("Opção inválida, por favor escolha novamente.")

def menu_principal():
    while True:
        print("--- Sistema de Gerenciamento de Adoção de Animais ---")
        print("1. Gerenciar Animais")
        print("2. Gerenciar Adotantes")
        print("3. Gerenciar Abrigos")
        print("4. Sugerir Correspondências de Adoção")
        print("5. Gerenciar Adoções")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        limpa_console()

        if opcao == '1':
            menu_animais()
        elif opcao == '2':
            menu_adotantes()
        elif opcao == '3':
            menu_abrigos()
        elif opcao == '4':
            sugerir_correspondencias()
        elif opcao == '5':
            menu_adoptions()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.\n")

def menu_animais():
    while True:
        print("--- Gerenciamento de Animais ---")
        print("1. Adicionar novo animal")
        print("2. Listar todos os animais")
        print("3. Atualizar um animal")
        print("4. Excluir um animal")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        limpa_console()

        if opcao == '1':
            animal = {
                "nome": input("Nome do animal: "),
                "especie": input("Espécie do animal: "),
                "raça": input("Raça do animal: "),
                "idade": input("Idade do animal: "),
                "personalidade": selecionar_personalidade(),
                "castrado": input("Castrado: (S/N) ").strip().upper() == "S",
                "foto": input("Foto (URL ou descrição): ")
            }

            limpa_console()

            shelterController.list_shelter()

            animal["abrigo_id"] = input("Escolha o id de um dos abrigos listados acima: ")

            animalsController.create_animal(animal)

            limpa_console()
        elif opcao == '2':
            animalsController.list_animals()
            print()
        elif opcao == '3':
            animalsController.list_animals()

            id = input("Escolha o ID de um dos animais listados acima para atualizar: ")

            print()

            animal = {
                "nome": input("Nome do animal: "),
                "especie": input("Espécie do animal: "),
                "raça": input("Raça do animal: "),
                "idade": input("Idade do animal: "),
                "personalidade": selecionar_personalidade(),
                "castrado": input("Castrado: (S/N) ").strip().upper() == "S",
                "foto": input("Foto (URL ou descrição): ")
            }

            limpa_console()

            shelterController.list_shelter()

            animal["abrigo_id"] = input("Digite o id de um dos abrigos listados acima: ")

            animalsController.update_animal(id, animal)

            limpa_console()
        elif opcao == '4':
            animalsController.list_animals()

            id = input("Escolha o ID de um dos animais listados acima para deletar: ")
            animalsController.delete_animal(id)
        
            limpa_console()
        elif opcao == '5':
            limpa_console()
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

def menu_adotantes():
    while True:
        print("--- Gerenciamento de Adotantes ---")
        print("1. Adicionar novo adotante")
        print("2. Listar todos os adotantes")
        print("3. Atualizar um adotante")
        print("4. Excluir um adotante")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        limpa_console()

        if opcao == '1':
            adotante = {
                "nome": input("Nome do adotante: "),
                "cidade": input("Cidade do adotante: "),
                "telefone": input("Telefone do adotante: "),
                "email": input("E-mail do adotante: "),
                "personalidade_desejada": selecionar_personalidade()
            }

            adoptersController.create_adopters(adotante)

            limpa_console()
        elif opcao == '2':
            adoptersController.list_adopters()
            print()
        elif opcao == '3':
            adoptersController.list_adopters()
            
            id = input("Escolha o ID de um dos adotantes listados acima para atualizar: ")

            adotante = {
                "nome": input("Novo nome do adotante: "),
                "cidade": input("Nova cidade do adotante: "),
                "telefone": input("Novo telefone do adotante: "),
                "email": input("Novo e-mail do adotante: "),
                "personalidade_desejada": selecionar_personalidade()
            }

            adoptersController.update_adopters(id, adotante)

            limpa_console()
        elif opcao == '4':
            adoptersController.list_adopters()

            id = input("Digite o ID do adotante que deseja excluir: ")

            adoptersController.delete_adopters(id)

            limpa_console()
        elif opcao == '5':
            limpa_console()
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

def menu_abrigos():
    while True:
        print("--- Gerenciamento de Abrigos ---")
        print("1. Adicionar novo abrigo")
        print("2. Listar todos os abrigos")
        print("3. Atualizar um abrigo")
        print("4. Excluir um abrigo")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        limpa_console()

        if opcao == '1':
            abrigo = {
                "nome": input("Nome do abrigo: "),
                "cidade": input("Cidade do abrigo: "),
                "telefone": input("Telefone do abrigo: "),
                "email": input("E-mail do abrigo: "),
                "capacidade": int(input("Capacidade máxima do abrigo: "))
            }

            shelterController.create_shelter(abrigo)

            limpa_console()
        elif opcao == '2':
            shelterController.list_shelter()
            print()
        elif opcao == '3':
            shelterController.list_shelter()

            id = input("Escolha o ID de um abrigo listado acima para atualizar: ")

            abrigo = {
                "nome": input("Novo nome do abrigo: "),
                "cidade": input("Nova cidade do abrigo: "),
                "telefone": input("Novo telefone do abrigo: "),
                "email": input("Novo e-mail do abrigo: "),
                "capacidade": int(input("Nova capacidade do abrigo: "))
            }

            shelterController.update_shelter(id, abrigo)

            limpa_console()
        elif opcao == '4':
            shelterController.list_shelter()

            id = input("Escolha o ID de um abrigo listado acima para deletar: ")

            shelterController.delete_shelter(id)

            limpa_console()
        elif opcao == '5':
            limpa_console()
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

def menu_adoptions():
    while True:
        print("--- Gerenciamento de Adoções ---")
        print("1. Realizar nova adoção")
        print("2. Listar todos as adoções")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        limpa_console()

        if opcao == 1:
            animalsController.list_animals()

            animal_id = input("Escolha o ID de um dos animais listados acima para adotar: ")

            limpa_console()

            adoptersController.list_adopters()

            adopter_id = input("Escolha o ID de um dos adotates para realizar a adoção: ")

            limpa_console()

            adoption_date = input("Digite a data de adoção: ")

            adoptionsController.create_adoption(animal_id, adopter_id, adoption_date)

            limpa_console()
        elif opcao == 2:
            adoptionsController.list_adoptions()
            print()
        elif opcao == 3:
            limpa_console()
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")


def sugerir_correspondencias():
    print("--- Sugerir Correspondências ---")

    database = databaseUtils.get_database()
    adotantes = database['adopters']
    animais = database['animals']
    abrigos = database['shelter']

    if not adotantes:
        print("Nenhum adotante cadastrado.")
        return
    if not animais:
        print("Nenhum animal cadastrado.")
        return
    if not abrigos:
        print("Nenhum abrigo cadastrado.")
        return

    for adotante_id, adotante in adotantes.items():
        print(
            f"\nSugestões para o adotante {adotante['nome']} (Cidade: {adotante['cidade']}, Personalidade desejada: {adotante['personalidade_desejada']}):")
        correspondencias_encontradas = False

        for animal_id, animal in animais.items():
            abrigo_id = animal.get("abrigo_id")
            abrigo = abrigos.get(abrigo_id, {})

            if abrigo and abrigo.get("cidade") == adotante["cidade"] and animal["personalidade"] == adotante[
                "personalidade_desejada"]:
                correspondencias_encontradas = True
                print(
                    f"- Animal: {animal['nome']} | Espécie: {animal['especie']} | Raça: {animal['raça']} | Personalidade: {animal['personalidade']} | Abrigo: {abrigo['nome']} | foto: {animal['foto']}")

        if not correspondencias_encontradas:
            print("Nenhuma correspondência encontrada para este adotante.")

    print("\nFim das sugestões.\n")

menu_principal()
