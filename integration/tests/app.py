from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://admin:adminpassword@localhost:27017/")
db = client.testdb
collection = db.testcollection

# Insertion de documents
collection.insert_one({"name": "Document from Python", "value": 30})

# Requêtes simples
for doc in collection.find({"value": {"$gt": 15}}):
    print(doc)

# Mise à jour
collection.update_one({"name": "Document from Python"}, {"$set": {"value": 35}})

# Suppression
collection.delete_one({"name": "Document from Python"})
