import json
from pathlib import Path


INDEX_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "applications_index.json"
)


class ApplicationFinder:

    def __init__(self):

        if not INDEX_FILE.exists():
            INDEX_FILE.write_text("{}")

    def find(self, app_name: str):

        app_name = app_name.lower().strip()

        print(f"Searching for: '{app_name}'")
        print(INDEX_FILE.resolve())
        with open(INDEX_FILE, "r") as f:
            data = json.load(f)

        print("Exists:", app_name in data)

        if app_name in data:
            print(data[app_name])

        return data.get(app_name)