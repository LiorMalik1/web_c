from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://malno:noamal2210@noa.ghwa7bo.mongodb.net/?retryWrites=true&w=majority&appName=noa"


class MongodbClientFactory:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = MongoClient(uri, server_api=ServerApi('1'))
        return cls._instance
