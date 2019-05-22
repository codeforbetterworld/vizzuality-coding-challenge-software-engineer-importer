from infrastructure import mongodbConnection
from pymongo.errors import DuplicateKeyError
import os

eget = os.environ.get

MONGO_APP_DATABASE_NAME=eget('MONGO_APP_DATABASE_NAME')

def save(data):
    mongodbConnection.initialize()
    mongoClient = mongodbConnection.createClient()
    database = mongoClient[MONGO_APP_DATABASE_NAME]
    try:
        database.emissions.insert(data, continue_on_error=False)
    except DuplicateKeyError:
        print('DuplicateKeyError')