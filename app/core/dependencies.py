from app.core.config import settings
from app.services.code_assistant_service import CodeAssistantService
from app.services.ollama_service import OllamaService

ollama_service = OllamaService(
    base_url=settings.ollama_base_url,
    model=settings.ollama_model,
    timeout=settings.ollama_timeout,
)

code_assistant_service = CodeAssistantService(
    ollama_service=ollama_service
)

def get_code_assistant_service() -> CodeAssistantService:
    return code_assistant_service

def get_ollama_service() -> OllamaService:
    return ollama_service
