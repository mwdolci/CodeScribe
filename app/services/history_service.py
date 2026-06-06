import json
from datetime import datetime
from pathlib import Path

class HistoryService:
    def __init__(self, file_path: str = "data/history.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(exist_ok=True)
        self.file_path.touch(exist_ok=True)

    def add_entry(self, action: str, input_code: str, result: str):
        history = self.get_history()

        history.append({
            "date": datetime.now().isoformat(timespec="seconds"),
            "action": action,
            "input": input_code,
            "result": result
        })

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)

    def get_history(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            return []