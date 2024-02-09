from pymongo import MongoClient
from typing import AnyStr
from decouple import config


class MongoDB:
    def __init__(self, db=None, *, collection: AnyStr):
        # client = MongoClient(
        #     host=config('DB_HOST', default='dj-app-mongo-container'),
        #     port=27017
        # )
        host = config('DB_HOST', default='db')
        user = 'mongosh'
        passwd = 'mongosh'

        # client = MongoClient(f"mongodb://{user}:{passwd}@{host}:27017/")
        client = MongoClient(f"mongodb://{host}:27017/")
        db = db or 'ecommerce'

        self.db = client[db]
        self.collection = self.db[collection]

    @property
    def get_collection(self):
        return self.collection

db = MongoDB
