import subprocess
import shutil
import os
from app.tools.base_tool import BaseTool
from app.indexer.application_finder import ApplicationFinder
from app.memory.memory_manager import MemoryManager


class AppLauncherTool(BaseTool):

    def __init__(self):
        self.memory = MemoryManager()
        self.finder = ApplicationFinder()

    @property
    def name(self):
        return "app_launcher"

    @property
    def description(self):
        return "Launches applications installed on the computer."

    @property
    def parameters(self):
        return {
            "app_name": {
                "type": "string",
                "description": "Application name to launch."
            }
        }
    def execute(self, app_name: str):
        
        app_name = app_name.lower().strip()

        # ---------------------------------
        # 1. Check Memory Cache
        # ---------------------------------

        cached_path = self.memory.get_application(app_name)

        if cached_path:
            try:
                os.startfile(cached_path)
                return f"Opening {app_name}."
            except Exception:
                # Cached path became invalid
                pass

        # ---------------------------------
        # 2. Check Application Index
        # ---------------------------------

        app = self.finder.find(app_name)
        print("Finder returned:", app)

        if app:

            self.memory.save_application(
                app_name,
                app["launch_path"]
            )

            try:

                if app["launch_type"] == "shortcut":

                    print("Launching shortcut...")
                    os.startfile(app["launch_path"])

                elif app["launch_type"] == "uwp":

                    print("Launching UWP...")

                    os.startfile(
                        f"shell:AppsFolder\\{app['launch_path']}"
                    )

                else:

                    print("Launching executable...")
                    subprocess.Popen(app["launch_path"])

                return f"Opening {app['display_name']}."

            except Exception as e:

                print(e)
                return f"Failed to open {app['display_name']}: {e}"
            # ---------------------------------
            # 3. Check Windows PATH
            # ---------------------------------

        program = shutil.which(app_name)

        if program:

            self.memory.save_application(
                app_name,
                program
            )

            try:
                subprocess.Popen(program)
                return f"Opening {app_name}."

            except Exception as e:
                return f"Failed to open {app_name}: {e}"

        # ---------------------------------
        # 4. Built-in Aliases
        # ---------------------------------

        aliases = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "calc": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "command prompt": "cmd.exe",
            "powershell": "powershell.exe",
            "explorer": "explorer.exe",
            "file explorer": "explorer.exe",
        }

        program = aliases.get(app_name)

        if program:

            self.memory.save_application(
                app_name,
                program
            )

            try:
                subprocess.Popen(program)
                return f"Opening {app_name}."

            except Exception as e:
                return f"Failed to open {app_name}: {e}"

        # ---------------------------------
        # 5. Not Found
        # ---------------------------------

        return f"I couldn't find '{app_name}' installed on this computer."