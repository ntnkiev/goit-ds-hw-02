from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import *

uri = "mongodb+srv://ntnkiev:mdb162263@cluster0.hu7npum.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
db = client.ds02

collection = db['cats']


def print_all_records(collection):
    try:
        all_records = collection.find()
    except Exception as e:
        print(e)
    for record in all_records:
        print(record)


def find_by_name(collection):
    name = input("Enter cat name: ")
    records = collection.find({"name": {"$eq": name}})
    for record in records:
        print(record)


def update_age_by_name(collection):
    name = input("Enter cat name: ")
    age = int(input("Enter cat age: "))
    collection.update_one({"name": name}, {"$set": {"age": age}}, upsert=False)
    print(f"Cat {name} age updated")


def add_features_by_name(collection):
    name = input("Enter cat name: ")
    feature = input("Enter cat feature: ")
    collection.update_one({"name": name}, {"$push": {"features": feature}})
    print(f"Cat {name} features added")


def delete_record_by_name(collection):
    name = input("Enter cat name: ")
    collection.delete_one({"name": name})
    print(f"Record {name} deleted")


def delete_all_records(collection):
    collection.delete_many({})
    print("All documents deleted.")


if __name__ == '__main__':
    # Реалізуйте функцію для виведення всіх записів із колекції
    print_all_records(collection)
    # Реалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
    find_by_name(collection)
    # Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.
    update_age_by_name(collection)
    # Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.
    add_features_by_name(collection)
    # Реалізуйте функцію для видалення запису з колекції за ім'ям тварини.
    delete_record_by_name(collection)
    # Реалізуйте функцію для видалення всіх записів із колекції.
    delete_all_records(collection)
