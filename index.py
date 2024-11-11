import adoptersController
import animalsController
import shelterController
import databaseUtils

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

def selecionar_personalidade():
    print("Selecione a personalidade:")
    for numero, descricao in personalidades_opcoes.items():
        print(f"{numero} - {descricao}")
    while True:
        try:
            escolha = int(input("Digite o número correspondente à personalidade: "))
            if escolha in personalidades_opcoes:
                return personalidades_opcoes[escolha]
            else:
                print("Opção inválida, por favor escolha novamente.")
        except ValueError:
            print("Entrada inválida, por favor insira um número.")

def menu_principal():
    while True:
        print("--- Sistema de Gerenciamento de Adoção de Animais ---")
        print("1. Gerenciar Animais")
        print("2. Gerenciar Adotantes")
        print("3. Gerenciar Abrigos")
        print("4. Sugerir Correspondências de Adoção")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_animais()
        elif opcao == '2':
            menu_adotantes()
        elif opcao == '3':
            menu_abrigos()
        elif opcao == '4':
            sugerir_correspondencias()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

def menu_animais():
    while True:
        print("--- Gerenciamento de Animais ---")
        print("1. Adicionar novo animal")
        print("2. Listar todos os animais")
        print("3. Atualizar um animal")
        print("4. Excluir um animal")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            animal = {
                "name": input("Nome do animal: "),
                "especie": input("Espécie do animal: "),
                "race": input("Raça do animal: "),
                "age": input("Idade do animal: "),
                "personalidade": selecionar_personalidade(),
                "castrado": input("Castrado: (S/N) ").strip().upper() == "S",
                "abrigo_id": input("ID do abrigo do animal: "),
                "foto": input("Foto (URL ou descrição): ")
            }
            animalsController.create_animal(animal)
        elif opcao == '2':
            animalsController.list_animals()
        elif opcao == '3':
            id = input("Digite o ID do animal que deseja atualizar: ")
            animal = {
                "name": input("Nome do animal: "),
                "especie": input("Espécie do animal: "),
                "race": input("Raça do animal: "),
                "age": input("Idade do animal: "),
                "personalidade": selecionar_personalidade(),
                "castrado": input("Castrado: (S/N) ").strip().upper() == "S",
                "abrigo_id": input("ID do abrigo do animal: "),
                "foto": input("Foto (URL ou descrição): ")
            }
            animalsController.update_animal(id, animal)
        elif opcao == '4':
            id = input("Digite o ID do animal que deseja excluir: ")
            animalsController.delete_animal(id)
        elif opcao == '5':
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

        if opcao == '1':
            adotante = {
                "name": input("Nome do adotante: "),
                "city": input("Cidade do adotante: "),
                "telefone": input("Telefone do adotante: "),
                "email": input("E-mail do adotante: "),
                "personalidade_desejada": selecionar_personalidade()
            }
            adoptersController.create_adopters(adotante)
        elif opcao == '2':
            adoptersController.list_adopters()
        elif opcao == '3':
            id = input("Digite o ID do adotante que deseja atualizar: ")
            adotante = {
                "name": input("Novo nome do adotante: "),
                "city": input("Nova cidade do adotante: "),
                "telefone": input("Novo telefone do adotante: "),
                "email": input("Novo e-mail do adotante: "),
                "personalidade_desejada": selecionar_personalidade()
            }
            adoptersController.update_adopters(id, adotante)
        elif opcao == '4':
            id = input("Digite o ID do adotante que deseja excluir: ")
            adoptersController.delete_adopters(id)
        elif opcao == '5':
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

        if opcao == '1':
            abrigo = {
                "name": input("Nome do abrigo: "),
                "city": input("Cidade do abrigo: "),
                "telefone": input("Telefone do abrigo: "),
                "email": input("E-mail do abrigo: "),
                "capacidade": int(input("Capacidade máxima do abrigo: "))
            }
            shelterController.create_shelter(abrigo)
        elif opcao == '2':
            shelterController.list_shelter()
        elif opcao == '3':
            id = input("Digite o ID do abrigo que deseja atualizar: ")
            abrigo = {
                "name": input("Novo nome do abrigo: "),
                "city": input("Nova cidade do abrigo: "),
                "telefone": input("Novo telefone do abrigo: "),
                "email": input("Novo e-mail do abrigo: "),
                "capacidade": int(input("Nova capacidade do abrigo: "))
            }
            shelterController.update_shelter(id, abrigo)
        elif opcao == '4':
            id = input("Digite o ID do abrigo que deseja excluir: ")
            shelterController.delete_shelter(id)
        elif opcao == '5':
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
            f"\nSugestões para o adotante {adotante['name']} (Cidade: {adotante['city']}, Personalidade desejada: {adotante['personalidade_desejada']}):")
        correspondencias_encontradas = False

        for animal_id, animal in animais.items():
            abrigo_id = animal.get("abrigo_id")
            abrigo = abrigos.get(abrigo_id, {})

            if abrigo and abrigo.get("city") == adotante["city"] and animal["personalidade"] == adotante[
                "personalidade_desejada"]:
                correspondencias_encontradas = True
                print(
                    f"- Animal: {animal['name']} | Espécie: {animal['especie']} | Raça: {animal['race']} | Personalidade: {animal['personalidade']} | Abrigo: {abrigo['name']}")

        if not correspondencias_encontradas:
            print("Nenhuma correspondência encontrada para este adotante.")

    print("\nFim das sugestões.")

if __name__ == "__main__":
    menu_principal()
