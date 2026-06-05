import re

from app.services.ollama_service import OllamaService

class CodeAssistantService:
    def __init__(self, ollama_service: OllamaService):
        self.ollama_service = ollama_service

    # Méthode utilitaire pour nettoyer les réponses de l'API Ollama
    def _clean_code_response(self, response: str) -> str:
        response = response.strip()

        # Si la réponse contient un bloc Markdown ```python ... ```
        match = re.search(r"```(?:\w+)?\s*\n?(.*?)```", response, re.DOTALL)
        if match:
            return match.group(1).strip()

        # Sinon, supprime les éventuels délimiteurs restants
        response = re.sub(r"^```(?:\w+)?\s*\n?", "", response)
        response = re.sub(r"\n?```$", "", response)

        return response.strip()

    async def comment_code(self, code: str, language: str) -> str:
        system_prompt = """
            Tu es CodeScribe, un assistant expert en programmation.

            RÈGLES OBLIGATOIRES :

            - Retourne uniquement le code final.
            - Ne fournis aucune explication avant le code.
            - Ne fournis aucune explication après le code.
            - Ne fournis aucun résumé.
            - N'utilise jamais les balises Markdown.
            - N'utilise jamais les délimiteurs ``` .
            - Le résultat doit être directement copiable dans un éditeur de code.
            - Conserve exactement le langage d'origine.
            - Ajoute uniquement des commentaires pertinents dans le code.
            - Les commentaires doivent être en français.
            - Ne modifie pas la logique du programme sauf si nécessaire pour ajouter les commentaires.

            Ta réponse doit contenir exclusivement du code commenté.
        """

        user_prompt = f"""
        Langage : {language}

        Commente chaque ligne du code suivant.
        Retourne uniquement le code commenté.

        Code :
        {code}
        """

        # Appel à l'API Ollama pour obtenir la réponse (await nécessaire pour les appels asynchrones)
        response = await self.ollama_service.chat(system_prompt, user_prompt)
        return self._clean_code_response(response)

    async def control_code(self, code: str, language: str) -> str:
        system_prompt = (
            "Tu es CodeScribe, un expert en revue de code. "
            "Tu détectes les erreurs et proposes des corrections."
        )

        user_prompt = f"""
        Langage : {language}

        Analyse le code suivant.
        Indique :
        1. Si le code est correct
        2. Les erreurs éventuelles
        3. Une version corrigée si nécessaire

        Code :
        {code}
        """

        return await self.ollama_service.chat(system_prompt, user_prompt)

    async def compress_code(self, code: str, language: str) -> str:
        system_prompt = (
            "Tu es CodeScribe, un assistant qui optimise le code. "
            "Tu réduis le nombre de lignes sans changer le comportement."
        )

        user_prompt = f"""
        Langage : {language}

        Compresse le code suivant.
        Garde le même comportement.
        Retourne uniquement le code optimisé.

        Code :
        {code}
        """

        response = await self.ollama_service.chat(system_prompt, user_prompt)
        return self._clean_code_response(response)