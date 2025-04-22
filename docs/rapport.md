# Rapport de TP : MongoDB

## Objectifs pédagogiques

- Comprendre les principes d’une base de données orientée document.
- Déployer MongoDB selon différents modes : standalone, replica set, puis sharding (bonus).
- Intégrer MongoDB dans une application avec un langage de votre choix.
- Documenter toutes les étapes de l’atelier dans un fichier Markdown.
- Versionner votre projet avec Git et le rendre accessible en ligne.

## Partie 1 – MongoDB Standalone

### Méthode de déploiement

Pour déployer MongoDB en mode standalone, nous avons utilisé Docker et Docker Compose. Voici les étapes suivies :

1. **Créer un répertoire pour le mode standalone** :
   ```bash
   mkdir -p mongo/standalone
   cd mongo/standalone
    ```
2. **Créer un fichier docker-compose.yml** :
    ```yaml
    services:
  mongodb:
    image: mongo:latest
    container_name: mongodb_standalone
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: adminpassword
    volumes:
      - mongo-data:/data/db

  mongo-client:
    image: mongo:latest
    container_name: mongo_client
    command: ["tail", "-f", "/dev/null"]
    depends_on:
      - mongodb

    volumes:
        mongo-data:
    ```
3. **Lancer le conteneur** :
    ```bash
    docker-compose up -d
    ```
**Création de l’utilisateur** :
    L'authentification est activée avec les variables d'environnement dans le fichier docker-compose.yml.

### Connexion à MongoDB :
Pour se connecter à MongoDB, nous avons utilisé mongosh (MongoDB Shell) :
```bash
docker exec -it mongo_client mongosh --username admin --password adminpassword --authenticationDatabase admin --host mongodb_standalone
```
### Commandes d’insertion, de requêtage, d’update et de suppression
1. **Créer une base de données et une collection** :
```mongosh
use testdb
db.createCollection("testcollection")
```
2. **Insérer des documents** :
```mongosh
db.testcollection.insertMany([
  { name: "Document 1", value: 10 },
  { name: "Document 2", value: 20 }
])
```
3. **Requêter des documents** :
```mongosh
db.testcollection.find()
```
4. **Mettre à jour un document** :
```mongosh
db.testcollection.updateOne({ name: "Document 1" }, { \$set: { value: 15 } })
```
5. **Supprimer un document** :
```mongosh
db.testcollection.deleteOne({ name: "Document 2" })
```
### Vérification avec une interface CLI ou graphique
Nous avons utilisé mongosh pour vérifier les données. Vous pouvez également utiliser MongoDB Compass pour une interface graphique.

## Partie 2 – MongoDB Replica Set
### Configuration des membres du replica set
Pour déployer un replica set, nous avons utilisé Docker Compose pour déployer trois instances MongoDB.
1. **Créer un fichier docker-compose.yml pour le replica set** :
   ```yaml
   services:
  mongo1:
    image: mongo\:latest
    container_name: mongo1
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27017:27017"
    volumes:
      - mongo1-data:/data/db

  mongo2:
    image: mongo\:latest
    container_name: mongo2
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27018:27017"
    volumes:
      - mongo2-data:/data/db

  mongo3:
    image: mongo\:latest
    container_name: mongo3
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27019:27017"
    volumes:
      - mongo3-data:/data/db

    volumes:
        mongo1-data:
        mongo2-data:
        mongo3-data:
   ```

2. **Lancer le conteneur** :
   ```bash
    docker-compose up -d
    ```
3. **Initialiser le replica set** :
   ```bash
   docker exec -it mongo1 mongosh
   ```
dans la console mongosh :
   ```mongosh
   rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})
```

### Explication des modes de lecture/écriture
Explication des modes de lecture/écriture
**PRIMARY** : Le seul nœud qui peut accepter les écritures.
**SECONDARY** : Les nœuds qui répliquent les données du PRIMARY et peuvent être utilisés pour les lectures.

### Insérer un document sur le PRIMARY, lire depuis un SECONDARY
1. **Insérer un document sur le PRIMARY** :
```bash
docker exec -it mongo1 mongosh
```
```mongosh
db.users.insertOne({ name: "John doe", role: "developer" })
```
2. **Lire depuis un SECONDARY** :
```bash
docker exec -it mongo2 mongosh
```
```mongosh
db.users.find()
```
## Partie 3 – Intégration dans une application

### Créer une application simple
Nous avons créé une application simple en Python pour se connecter à MongoDB.

1. **Installer les dépendances** :
```bash
pip install pymongo
```
2. **Créer un fichier app.py** :
```python
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
```
3. **Exécuter l’application** :
```bash
python app.py
```
### Vérification des données
nous avons executer le script sur le standalone et nous avons obtenu le resultat suivant au terminal
```bash
$ python app.py
{'_id': ObjectId('68078b2648a517cad1d861e1'), 'name': 'Document 2', 'value': 20}
{'_id': ObjectId('6807a4abb28103339fd32118'), 'name': 'Document from Python', 'value': 30}
```


