import databaseUtils
import uuid


def create_shelter(shelter):
    database = databaseUtils.get_database()

    shelter_id = uuid.uuid4()
    database['shelter'][str(shelter_id)] = shelter

    databaseUtils.set_database(database)