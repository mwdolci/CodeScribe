from dataclasses import dataclass
import os


def _to_bool(value: str, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(slots=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "CodeScribe API")
    app_env: str = os.getenv("APP_ENV", "development")
    debug: bool = _to_bool(os.getenv("DEBUG"), default=True)
    history_data_path: str = os.getenv("HISTORY_DATA_PATH", "data/history.json")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.2")
    ollama_timeout: float = float(os.getenv("OLLAMA_TIMEOUT", "60"))


settings = Settings()
