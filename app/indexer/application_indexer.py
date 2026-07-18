import json
import os
from datetime import datetime
from pathlib import Path

IGNORE_EXECUTABLES = {
    "service",
    "helper",
    "bootstrapper",
    "installer",
    "uninstaller",
    "updater",
    "update",
    "crashpad_handler",
    "gpu_check",
    "gpu_memory_check",
    "minizip",
    "zucchini",
    "nvapi",
    "bstrace",
    "crosvm",
}

INDEX_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "applications_index.json"
)


SEARCH_DIRECTORIES = [
    os.environ.get("PROGRAMFILES"),
    os.environ.get("PROGRAMFILES(X86)"),
    os.environ.get("LOCALAPPDATA"),
]


class ApplicationIndexer:

    def __init__(self):

        INDEX_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not INDEX_FILE.exists():
            INDEX_FILE.write_text("{}")

    def _load(self):

        with open(INDEX_FILE, "r") as f:
            return json.load(f)

    def _save(self, data):

        with open(INDEX_FILE, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )
    def normalize_name(self, name: str) -> str:
        """Convert executable/folder names into a friendly searchable name."""

        return (
            name.lower()
                .replace("_", " ")
                .replace("-", " ")
                .strip()
        )


    def is_valid_executable(self, exe_name: str) -> bool:

        exe_name = Path(exe_name).stem.lower()

        if exe_name in IGNORE_EXECUTABLES:
            return False

        return True


    def choose_best_executable(self, folder_name, executables):

        if not executables:
            return None

        folder = self.normalize_name(folder_name)

        best = None
        best_score = -1

        for exe in executables:

            exe_name = Path(exe).stem

            score = 0

            normalized = self.normalize_name(exe_name)

            # Exact folder match gets highest priority
            if normalized == folder:
                score += 100

            # Partial match
            elif folder in normalized:
                score += 70

            # Longer names are usually more descriptive
            score += len(normalized)

            if score > best_score:
                best_score = score
                best = exe

        return best
    
    def build_index(self):

        data = {}

        for directory in SEARCH_DIRECTORIES:

            if not directory:
                continue

            if not os.path.exists(directory):
                continue

            print(f"Scanning: {directory}")

            for root, dirs, files in os.walk(directory):

                # Collect valid executables in this folder
                executables = []

                for file in files:

                    if not file.lower().endswith(".exe"):
                        continue

                    if not self.is_valid_executable(file):
                        continue

                    executables.append(file)

                if not executables:
                    continue

                # Choose the best executable from this folder
                best = self.choose_best_executable(
                    os.path.basename(root),
                    executables
                )

                if not best:
                    continue

                app_name = self.normalize_name(
                    os.path.basename(root)
                )

                if app_name in data:
                    continue

                data[app_name] = {
                    "name": os.path.basename(root),
                    "path": os.path.join(root, best),
                    "folder": os.path.basename(root),
                    "last_verified": datetime.now().isoformat()
                }

        self._save(data)

        print(f"Indexed {len(data)} applications.")