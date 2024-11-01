import os
import json
from textwrap import indent

DATABASE_FILENAME = './database.json'
FILE_INDENTATION = 2

def init_database():
    with open(DATABASE_FILENAME, 'w') as database_file:
        json.dump({
            "animals": {}
        }, database_file, indent=FILE_INDENTATION)

def get_database():
    if not os.path.exists(DATABASE_FILENAME):
        init_database()

    with open(DATABASE_FILENAME, 'r') as database_file:
        database = json.load(database_file)
        return database

def set_database(database):
    if not os.path.exists(DATABASE_FILENAME):
        init_database()

    with open(DATABASE_FILENAME, 'w') as database_file:
        json.dump(database, database_file, indent=FILE_INDENTATION)