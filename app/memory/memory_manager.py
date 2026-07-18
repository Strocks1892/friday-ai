import json
from pathlib import Path


CACHE_FILE = (
    Path(__file__).parent
    / "cache"
    / "applications.json"
)


class MemoryManager:

    def __init__(self):

        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

        if not CACHE_FILE.exists():
            CACHE_FILE.write_text("{}")

    def _load(self):

        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save(self, data):

        with open(CACHE_FILE, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

    def get_application(self, app_name):

        data = self._load()

        return data.get(app_name.lower())

    def save_application(self, app_name, path):

        data = self._load()

        data[app_name.lower()] = path

        self._save(data)