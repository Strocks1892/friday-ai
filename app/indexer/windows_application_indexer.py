import os
from pathlib import Path
import json

INDEX_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "applications_index.json"
)

START_MENU_LOCATIONS = [
    Path(os.environ["PROGRAMDATA"])
    / "Microsoft"
    / "Windows"
    / "Start Menu"
    / "Programs",

    Path(os.environ["APPDATA"])
    / "Microsoft"
    / "Windows"
    / "Start Menu"
    / "Programs",
]


class StartMenuIndexer:

    def scan(self):

        applications = {}

        for location in START_MENU_LOCATIONS:

            if not location.exists():
                continue

            print(f"Scanning Start Menu: {location}")

            for root, dirs, files in os.walk(location):

                for file in files:

                    if not file.lower().endswith(".lnk"):
                        continue

                    app_name = Path(file).stem.strip()
                    
                    key = app_name.lower()
                    
                    if key not in applications:
                        applications[key] = {
                            "display_name": app_name,
                            "launch_path": str(Path(root) / file),
                            "launch_type": "shortcut",
                            "source": "start_menu"
                        }
        with open(INDEX_FILE, "w") as f:
            json.dump(
                applications,
                f,
                indent=4
            )

        print(f"Indexed {len(applications)} Start Menu applications.")

        return applications