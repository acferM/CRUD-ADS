import databaseUtils
import uuid


def create_shelter(shelter):
    database = databaseUtils.get_database()

    shelter_id = uuid.uuid4()
    database['shelter'][str(shelter_id)] = shelter

    databaseUtils.set_database(database)

def list_shelter():
    database = databaseUtils.get_database()

    for shelter_id in database['shelter']:
        shelter = database['shelter'][shelter_id]

        print(f'id: {shelter_id}')
        print(f'name: {shelter["name"]}')
        print(f'city: {shelter["city"]}')
        print(f'telefone: {shelter["telefone"]}')
        print(f'email: {shelter["email"]}')
        print(f'capacidade: {shelter["capacidade"]}')
        print('-' * 40)

def update_shelter(id, shelter):
    database = databaseUtils.get_database()

    if not id in database['shelter']:
        print('Nenhum abrigo encontrado com esse id')
        return

    database['shelter'][id] = shelter
    databaseUtils.set_database(database)

def delete_shelter(id):
    database = databaseUtils.get_database()

    if not id in database['shelter']:
        print('Nenhum abrigo encontrado com esse id')
        return

    del database['shelter'][id]
    databaseUtils.set_database(database)