import os
from pymongo import MongoClient

MONGO_HOST = os.environ.get('MELI_AUTH_MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MELI_AUTH_MONGO_PORT', 27017)
MONGO_DB = os.environ.get('MELI_AUTH_MONGO_DB')
MONGO_COLLECTION = os.environ.get('MELI_AUTH_MONGO_COLLECTION')


def mongo_connection(fn):
    def wraps(*args, **kwargs):
        client = MongoClient(
            host=MONGO_HOST,
            port=int(MONGO_PORT)
        )
        return fn(client, *args, **kwargs)
    return wraps


@mongo_connection
def save_user(client, data):
    collection = client[MONGO_DB][MONGO_COLLECTION]
    query = {'user_id': data['user_id']}
    existing = collection.find_one(query)
    if existing:  # Remove existing entries to avoid document creep
        collection.remove(query)
    result = collection.insert_one(data)
    return result


@mongo_connection
def get_token(client, user_id):
    collection = client[MONGO_DB][MONGO_COLLECTION]
    query = {'user_id': user_id}
    return collection.find_one(query)
