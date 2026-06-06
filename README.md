# CodeScribe

## Description

CodeScribe est une application web développée avec **FastAPI** et **Ollama** permettant d'analyser du code source à l'aide d'un modèle d'intelligence artificielle générative.

L'utilisateur peut coller ou écrire du code dans une interface web puis demander à l'IA de :

* commenter le code ligne par ligne ;
* vérifier la qualité et la validité du code ;
* proposer une version optimisée et plus concise du code.

Le projet a été réalisé dans le cadre de la formation **MAS-RAD**.

---

## Auteur

Marco Dolci

## Fonctionnalités

### Commenter du code

L'IA analyse le code fourni et ajoute des commentaires explicatifs afin d'améliorer sa compréhension.

### Contrôler du code

L'IA vérifie le code et signale :

* les erreurs potentielles ;
* les mauvaises pratiques ;
* les améliorations possibles.

### Compresser du code

L'IA propose une version plus concise du code tout en conservant le même comportement fonctionnel.

### Documentation automatique

L'API expose automatiquement une documentation Swagger accessible via :

```text
http://localhost:8000/docs
```

---

## Architecture du projet

```text
CodeScribe/
│
├── app/
│   ├── core/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── img/
│   ├── index.html
│   ├── control.html
│   └── compress.html
│
├── data/
│   └── history.json
│
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Architecture du projet avec détails

```text
CodeScribe/
│
├── app/
│   │
│   ├── main.py
│   │   └── Point d'entrée de l'application FastAPI.
│   │
│   ├── core/
│   │   ├── config.py
│   │   │   └── Gestion de la configuration de l'application.
│   │   │
│   │   ├── dependencies.py
│   │   │   └── Déclaration et injection des dépendances.
│   │   │
│   │   └── factory.py
│   │       └── Création et initialisation des services métier.
│   │
│   ├── routers/
│   │   ├── code.py
│   │   │   └── Endpoints API pour commenter, contrôler et compresser du code.
│   │   │
│   │   └── health.py
│   │       └── Endpoint de vérification de disponibilité de l'API.
│   │
│   ├── schemas/
│   │   └── code.py
│   │       └── Modèles Pydantic utilisés par les requêtes API.
│   │
│   └── services/
│       ├── code_assistant_service.py
│       │   └── Construction des prompts et logique métier.
│       │
│       ├── ollama_service.py
│       │    └── Communication avec Ollama et exécution des requêtes LLM.
│       │
│		└── history_service.py
│            └── Mémorisation des conversations.
│
├── frontend/
│   │
│   ├── index.html
│   │   └── Page de commentaire automatique du code.
│   │
│   ├── control.html
│   │   └── Page d'analyse et de contrôle qualité du code.
│   │
│   ├── compress.html
│   │   └── Page de compression et d'optimisation du code.
│   │
│   ├── settings.html
│   │   └── Paramétrage des préférences utilisateur.
│   │
│   ├── privacy.html
│   │   └── Politique de confidentialité de l'application.
│   │
│   ├── css/
│   │   └── style.css
│   │       └── Feuille de style principale de l'interface.
│   │
│   ├── js/
│   │   ├── api.js
│   │   │   └── Gestion des appels API vers le backend.
│   │   │
│   │   ├── layout.js
│   │   │   └── Gestion du menu de navigation et des composants communs.
│   │   │
│   │   └── settings.js
│   │       └── Sauvegarde et chargement des préférences utilisateur.
│   │
│   └── img/
│       ├── logo.png
│       │   └── Logo principal de CodeScribe.
│       │
│       └── mini_logo.png
│           └── Icône utilisée dans l'interface.
│
├── data/
│   └── history.json
│       └── Stockage local de l'historique des opérations.
│
├── Dockerfile
│   └── Construction de l'image Docker du backend.
│
├── compose.yaml
│   └── Orchestration des conteneurs Docker (API et Ollama).
│
├── requirements.txt
│   └── Liste des dépendances Python du projet.
│
├── README.md
│   └── Documentation du projet.
│
├── LICENSE
│   └── Licence du projet.
│
├── .env
│   └── Variables d'environnement de l'application.
│
├── .dockerignore
│   └── Fichiers exclus du contexte de build Docker.
│
└── .gitignore
    └── Fichiers ignorés par Git.
```


## Technologies utilisées

### Backend

* Python 3.11
* FastAPI
* Pydantic
* HTTPX

### Intelligence Artificielle

* Ollama
* Llama 3.2

### Frontend

* HTML5/Bootstrap
* CSS3
* JavaScript

### Conteneurisation

* Docker
* Docker Compose

---

## Installation

### Prérequis

Installer :

* Docker Desktop
* Ollama

Télécharger le modèle :

```bash
ollama pull llama3.2
```

---

## Lancement du projet

Depuis la racine du projet :

```bash
docker compose up --build
```

Une fois les conteneurs démarrés :

Application :

```text
http://localhost:8000
```

Documentation Swagger :

```text
http://localhost:8000/docs
```

---

## Endpoints disponibles

### Vérification de l'état de l'application

```http
GET /health
```

Réponse :

```json
{
  "status": "ok"
}
```

---

### Commenter du code

```http
POST /api/comment
```

Exemple :

```json
{
  "code": "def add(a,b):\n    return a+b",
  "language": "python"
}
```

---

### Contrôler du code

```http
POST /api/control
```

Exemple :

```json
{
  "code": "print(test)",
  "language": "python"
}
```

---

### Compresser du code

```http
POST /api/compress
```

Exemple :

```json
{
  "code": "x = 1\ny = 2\nprint(x + y)",
  "language": "python"
}
```

---

## Gestion des erreurs

L'application gère :

* les erreurs HTTP ;
* les erreurs de validation JSON ;
* les erreurs utilisateur ;
* les erreurs de communication avec Ollama ;
* les réponses invalides du modèle d'IA.

---

## Prompt Engineering

Le projet utilise des prompts spécialisés selon l'action demandée :

* commentaire de code ;
* revue de code ;
* optimisation et compression de code.

Chaque fonctionnalité possède son propre contexte système afin d'obtenir des réponses adaptées.

---

## Historique

L'application conserve un historique minimal des requêtes et réponses dans le fichier :

```text
data/history.json
```

Il peut être consulter sous : http://localhost:8000/api/history

---



