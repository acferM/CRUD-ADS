import databaseUtils
import uuid


def create_animal(animal):
    database = databaseUtils.get_database()

    animal_id = uuid.uuid4()
    database['animals'][str(animal_id)] = animal

    databaseUtils.set_database(database)

def list_animals():
    database = databaseUtils.get_database()

    for animal_id in database['animals']:
        animal = database['animals'][animal_id]

        print(f'id: {animal_id}')
        print(f'name: {animal["name"]}')
        print(f'race: {animal["race"]}')
        print('-' * 20)

def update_animal(id, animal):
    database = databaseUtils.get_database()

    if not id in database['animals']:
        print('Nenhum animal encontrado com esse id')
        return

    database['animals'][id] = animal
    databaseUtils.set_database(database)

def delete_animal(id):
    database = databaseUtils.get_database()

    if not id in database['animals']:
        print('Nenhum animal encontrado com esse id')
        return

    del database['animals'][id]
    databaseUtils.set_database(database)