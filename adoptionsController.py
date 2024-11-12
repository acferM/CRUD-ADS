import uuid
import databaseUtils


def create_adoption(animal_id, adopter_id, adoption_date):
    database = databaseUtils.get_database()

    if not animal_id in database['animals']:
        print('Nenhum animal encontrado com esse id')
        return

    if not adopter_id in database['adopters']:
        print('Nenhum adotante encontrado com esse id')
        return

    animal = database['animals'][animal_id]
    adopter = database['adopters'][adopter_id]

    adoption_id = uuid.uuid4()

    adoption = {
        "animal": animal,
        "adopter": adopter,
        "adoption_date": adoption_date
    }

    del database['animals'][animal_id]

    database['adoptions'][str(adoption_id)] = adoption

    databaseUtils.set_database(database)

def list_adoptions():
    database = databaseUtils.get_database()

    for adoption_id in database['adoptions']:
        adoption = database['adoptions'][adoption_id]

        print(f'id: {adoption_id}')
        print(f'animal: {adoption["animal"]}')
        print(f'adotante: {adoption["adopter"]}')
        print(f'data de adoção: {adoption["adoption_date"]}')
        print('-' * 40)