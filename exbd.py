import pymongo
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb+srv://INES:ziedines@cluster0.hzogq.mongodb.net/")
db = client["tp_python_mongo"]
collection = db["clients"]

# Jeu de données
clients_data = [
    {"id": 1, "nom": "Alice", "age": 30, "ville": "Paris", "depenses": 1500},
    {"id": 2, "nom": "Bob", "age": 25, "ville": "Lyon", "depenses": 1200},
    {"id": 3, "nom": "Charlie", "age": 35, "ville": "Marseille", "depenses": 800},
    {"id": 4, "nom": "Diana", "age": 28, "ville": "Toulouse", "depenses": 950},
]

# Insérer les données dans MongoDB
collection.insert_many(clients_data)
print("Données insérées dans MongoDB.")

#2. Extraire et structurer les données 


# Extraction des données
data = list(collection.find())

# Structuration des données
liste_clients = [client["nom"] for client in data]
dictionnaire_clients = {client["id"]: client for client in data}
tuples_clients = [(client["nom"], client["age"], client["ville"]) for client in data]

print("Liste des clients :", liste_clients)
print("Dictionnaire des clients :", dictionnaire_clients)
print("Tuples des clients :", tuples_clients)


#3.Calculez l'âge moyen et les dépenses moyennes des clients.


import statistics

ages = [client["age"] for client in data]
depenses = [client["depenses"] for client in data]

age_moyen = statistics.mean(ages)
depenses_moyennes = statistics.mean(depenses)

print(f"Âge moyen : {age_moyen}")
print(f"Dépenses moyennes : {depenses_moyennes}")

#4. Recherche de tendances

 #Identifiez les clients ayant dépensé plus de 1 000 unités.
grands_depensiers = [client for client in data if client["depenses"] > 1000]

print("Clients ayant dépensé plus de 1 000 unités :")
for client in grands_depensiers:
    print(client["nom"], "-", client["depenses"])
