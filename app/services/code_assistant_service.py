from app.services.ollama_service import OllamaService

class CodeAssistantService:
    def __init__(self, ollama_service: OllamaService):
        self.ollama_service = ollama_service

    async def comment_code(self, code: str, language: str) -> str:
        system_prompt = (
            "Tu es CodeScribe, un assistant IA spécialisé en programmation. "
            "Tu expliques le code clairement en français."
        )

        user_prompt = f"""
        Langage : {language}

        Commente chaque ligne du code suivant.
        Retourne uniquement le code commenté.

        Code :
        {code}
        """

        return await self.ollama_service.chat(system_prompt, user_prompt) # Appel à l'API Ollama pour obtenir la réponse (await nécessaire pour les appels asynchrones)

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

        return await self.ollama_service.chat(system_prompt, user_prompt)