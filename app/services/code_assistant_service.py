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

    async def comment_code(self, code: str, comment_level: str, max_comment_length: int) -> str:
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
            Analyse le code suivant.

            1. Détecte automatiquement le langage utilisé.
            2. Ajoute des commentaires adaptés à ce langage.
            3. Les commentaires doivent être en français.
            4. Retourne uniquement le code commenté.
            5. N'utilise jamais de markdown.
            6. N'utilise jamais ```.

            Niveau de détail demandé (1=bref, 2=normal, 3=détaillé) :
            {comment_level}

            Chaque commentaire individuel doit contenir au maximum {max_comment_length} caractères.

            Code :
            {code}
        """

        # Pour debug. Contrôle si prompt tient compte des settings du frontend.
        print("Prompt envoyé à Ollama :")
        print(user_prompt)

        # Appel à l'API Ollama pour obtenir la réponse (await nécessaire pour les appels asynchrones)
        response = await self.ollama_service.chat(system_prompt, user_prompt)
        return self._clean_code_response(response)

    async def control_code(self, code: str) -> str:
        system_prompt = (
            "Tu es CodeScribe, un expert en revue de code. "
            "Tu détectes les erreurs et proposes des corrections."
        )

        user_prompt = f"""
            Analyse le code suivant.

            1. Détecte automatiquement le langage.
            2. Vérifie la syntaxe et la logique.
            3. Signale les erreurs éventuelles.
            4. Propose une correction si nécessaire.

            Code :
            {code}
        """

        return await self.ollama_service.chat(system_prompt, user_prompt)

    async def compress_code(self, code: str) -> str:
        system_prompt = (
            "Tu es CodeScribe, un assistant qui optimise le code. "
            "Tu réduis le nombre de lignes sans changer le comportement."
        )

        user_prompt = f"""
            Analyse le code suivant.

            1. Détecte automatiquement le langage.
            2. Optimise et réduit le nombre de lignes.
            3. Conserve exactement le même comportement.
            4. Retourne uniquement le code optimisé.
            5. N'utilise jamais de markdown.

            Code :
            {code}
        """

        response = await self.ollama_service.chat(system_prompt, user_prompt)
        return self._clean_code_response(response)