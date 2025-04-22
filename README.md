# Objectifs pédagogiques
Comprendre les principes d’une base de données orientée document

Déployer MongoDB selon différents modes : standalone, replica set, puis sharding (bonus)

Intégrer MongoDB dans une application avec un langage de votre choix

Documenter toutes les étapes de l’atelier dans un fichier Markdown

Versionner votre projet avec Git et le rendre accessible en ligne. M'ajouter comme collaborateur (alexandre.chaussier@ynov.com)



# Consignes générales
Vous pouvez utiliser Docker/Docker Compose pour vos déploiements, mais ce n’est pas obligatoire

Chaque mode de déploiement doit être isolé dans un dossier propre

Vous devez documenter l’atelier dans un fichier Markdown (docs/rapport.md) incluant :

Les étapes réalisées pour chaque mode

Les commandes utilisées

Les résultats obtenus et leur interprétation

Les éventuels problèmes rencontrés et leur résolution

Vous devez intégrer MongoDB avec un langage de votre choix (Python, JavaScript, Go, etc.)

Documentez les méthodes de connexion, et commentez les alternatives possibles (localhost, URI avec authentification, replica set, mongos, etc.)



## 📁 Structure de projet recommandée
atelier-mongodb/
├── docs/
│   └── rapport.md
├── mongo/
│   ├── standalone/
│   ├── replicaset/
│   └── sharding/         # Bonus
├── integration/
│   └── <langage>/
│       └── tests/
└── README.md
## 🧩 Partie 1 – MongoDB Standalone
Installer MongoDB sur une machine ou dans un conteneur

Activer l’authentification et créer un utilisateur admin

Créer une base testdb avec une collection de test

Ajouter quelques documents, faire quelques requêtes

Vérifier le fonctionnement avec une interface CLI ou graphique (mongosh, Compass…)

À documenter :

Méthode de déploiement

Création de l’utilisateur

Connexion à la base (plusieurs méthodes possibles)

Commandes d’insertion, de requêtage, d’update et de suppression



## 🧪 Partie 2 – MongoDB Replica Set
Déployer au moins 3 instances MongoDB en replica set

Initialiser le replica set (via script ou ligne de commande)

Vérifier les rôles (PRIMARY, SECONDARY) via rs.status()

Insérer un document sur le PRIMARY, lire depuis un SECONDARY

À documenter :

Configuration des membres du replica set

Méthodes d’initialisation

Connexions possibles (URI avec replicaSet, readPreference, etc.)

Explication des modes de lecture/écriture



## ⚙️ Partie 3 – Intégration dans une application
Créer une application simple qui se connecte à MongoDB

Réaliser les actions suivantes :

Connexion sécurisée

Insertion de documents

Requêtes simples avec filtres

Mise à jour et suppression

Tester l’application avec la base standalone ou replica set

Commenter les méthodes de connexion possibles selon les cas

À documenter :

Code de connexion avec commentaires (expliquer l’URI)

Code des actions réalisées

Dépendances utilisées

Résultats des tests (prints, screenshots ou tests automatisés)

## 🌐 Partie 4 – Sharding (bonus)
Déployer :

3 shards (au minimum avec 1 instance chacun)

1 ou 3 config servers

1 mongos router

Activer le sharding sur une base nommée sharddb

Définir une clé de sharding sur une collection

Insérer des documents et observer la distribution avec sh.status()

À documenter :

Architecture choisie

Scripts ou commandes utilisés

Raisonnement autour de la clé de sharding

Observations sur la distribution

