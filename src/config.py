from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/mydatabase"
client = MongoClient(MONGO_URI)
db = client.mydatabase
