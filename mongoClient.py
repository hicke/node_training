from pymongo import MongoClient

client = MongoClient('localhost', 32774)
db = client.testDatabase
collection = db.testCollection

