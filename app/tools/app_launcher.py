import os
import subprocess

from app.tools.base_tool import BaseTool


class AppLauncherTool(BaseTool):

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

        apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "powershell": "powershell.exe",
        }

        app = apps.get(app_name.lower())

        if not app:
            return f"I couldn't find an application named '{app_name}'."

        try:
            subprocess.Popen(app)
            return f"Opening {app_name}."

        except Exception as e:
            return f"Failed to open {app_name}: {e}"