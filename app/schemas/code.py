# Ce fichier contient les schémas de données pour les requêtes et réponses liées au code.
# Il utilise Pydantic pour définir les modèles de données, assurant la validation et la sérialisation des données.
from pydantic import BaseModel, Field


# Schéma pour la requête de code, incluant le code lui-même et les paramètre de configuration du frontend
class CodeRequest(BaseModel):
    code: str = Field(..., min_length=1, description="Code envoyé par l'utilisateur")

    comment_level: str = "normal"
    max_comment_length: int = 120

    compression_level: str = "2"


# Schéma pour la réponse du code, incluant l'action effectuée et le résultat de l'exécution du code.
class CodeResponse(BaseModel):
    action: str
    result: str
