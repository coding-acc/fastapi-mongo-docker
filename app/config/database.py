from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")


client = MongoClient(config.get("DATABASE_CONNECTION_URL"))
db = client.test

collection = db["test_collection"]
#"mongodb+srv://kameersookoo:@cluster0.frjq7mg.mongodb.net/?retryWrites=true&w=majority"