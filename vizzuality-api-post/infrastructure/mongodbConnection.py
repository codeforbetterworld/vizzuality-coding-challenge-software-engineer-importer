from pymongo import MongoClient
from threading import Thread
import os

eget = os.environ.get
MONGO_HOST=eget('MONGO_HOST')
MONGO_PORT=eget('MONGO_PORT')
MONGO_APP_USER=eget('MONGO_APP_USER')
MONGO_APP_USER_PASSWORD=eget('MONGO_APP_USER_PASSWORD')
MONGO_APP_DATABASE_NAME=eget('MONGO_APP_DATABASE_NAME')

def initialize():
    mongoClient = createClient()
    if(not databaseExists(mongoClient)):
        createDatabaseAndCollection(mongoClient)

def databaseExists(mongoClient):
    for p in mongoClient.list_databases():
        if(MONGO_APP_DATABASE_NAME == p['name']):
            return True
    return False

def createDatabaseAndCollection(mongoClient):
    try:
        database = mongoClient[MONGO_APP_DATABASE_NAME]
        item = {
            "test": "test"
        }
        database.emissions.insert_one(item)
        database.emissions.delete_many({})
    except:
        print('Error initializing database')

def createClient():
    mongoClient = MongoClient('mongodb://'
                                + str(MONGO_APP_USER)
                                + ':'
                                + str(MONGO_APP_USER_PASSWORD)
                                + '@'
                                + str(MONGO_HOST)
                                + ':'
                                + MONGO_PORT
                                + '/admin')
    return mongoClient

initialize()