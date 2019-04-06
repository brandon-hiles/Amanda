__version__ = 0.3
__author__ = "Brandon Hiles"

from pymongo import MongoClient

class Mongo(object):

    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.db = MongoClient(self.host, self.port)[database]

    def select_collection(self, db, collection):
        return self.db[collection]

    def check_collection(self, collection, query):
        # Check if collection exists in db

        collection = self.select_collection(db=db, collection=collection)
        result = collection.find(query)
        if collection.find(query).count() > 0:
            return True
        else:
            return False

    def check_database_by_url(self, collection, url):

        collection = self.select_collection(collection=collection)
        urls = []
        for url_data in collection.find({'url' : url}):
            urls.append(url_data)
        return urls

    def add_index(self, collection, parms=["names", "articles"]):
        # parms is an array of elements

        collection.createIndex({ parms[0] : "text", parms[1] : "text"});
