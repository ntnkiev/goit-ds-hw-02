
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ntnkiev:mdb162263@cluster0.hu7npum.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
db = client.ds02

try:
    db.cats.insert_one({
        "name": 'barsik',
        "age": 3,
        "features": ['ходить в капці', 'дає себе гладити', 'рудий'],
    })
    print("Successfully added")
except Exception as e:
    print(e)