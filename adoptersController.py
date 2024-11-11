import databaseUtils
import uuid


def create_adopters(adopters):
    database = databaseUtils.get_database()

    adopters_id = uuid.uuid4()
    database['adopters'][str(adopters_id)] = adopters

    databaseUtils.set_database(database)

def list_adopters():
    database = databaseUtils.get_database()

    for adopters_id in database['adopters']:
        adopters = database['adopters'][adopters_id]

        print(f'id: {adopters_id}')
        print(f'name: {adopters["name"]}')
        print(f'city: {adopters["city"]}')
        print(f'telefone: {adopters["telefone"]}')
        print(f'email: {adopters["email"]}')
        print(f'personalidade_desejada: {adopters["personalidade_desejada"]}')
        print('-' * 20)

def update_adopters(id, adopters):
    database = databaseUtils.get_database()

    if not id in database['adopters']:
        print('Nenhum adotante encontrado com esse id')
        return

    database['adopters'][id] = adopters
    databaseUtils.set_database(database)

def delete_adopters(id):
    database = databaseUtils.get_database()

    if not id in database['adopters']:
        print('Nenhum adotante encontrado com esse id')
        return

    del database['adopters'][id]
    databaseUtils.set_database(database)