import json
import subprocess
from pathlib import Path


INDEX_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "applications_index.json"
)


class UWPIndexer:

    def scan(self):

        command = [
            "powershell",
            "-Command",
            "Get-StartApps | ConvertTo-Json"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if not result.stdout.strip():
            return {}

        apps = json.loads(result.stdout)

        if isinstance(apps, dict):
            apps = [apps]

        applications = {}

        for app in apps:

            name = app.get("Name", "").strip()
            app_id = app.get("AppID", "").strip()

            if not name:
                continue

            applications[name.lower()] = {
                "display_name": name,
                "launch_path": app_id,
                "launch_type": "uwp",
                "source": "uwp"
            }

        # -----------------------------
        # Save to applications_index.json
        # -----------------------------

        INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(
            INDEX_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                applications,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Indexed {len(applications)} UWP applications.")

        return applications