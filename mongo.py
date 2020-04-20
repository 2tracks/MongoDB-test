import pymongo
import os


if os.path.exists("env.py"):
    import env


MONGODB_URI = os.getenv("MONGODB_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_color': 'grey', 'occupation':'writer', 'nationality': 'elglish'}
#new_doc = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_color': 'not much', 'occupation':'writer', 'nationality': 'elglish'},
#{'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'hair_color': 'white', 'occupation':'writer', 'nationality': 'american'}]


#coll.insert_many(new_doc)

#documents = coll.remove({'first': 'douglas'})
coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
documents = coll.find()

for doc in documents:
    print(doc)
