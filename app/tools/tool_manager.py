from app.tools.calculator import CalculatorTool
from app.tools.date_time_tool import DateTimeTool
from app.tools.app_launcher import AppLauncherTool


class ToolManager:

    def __init__(self):

        self.tools = {}

        self.register(CalculatorTool())
        self.register(DateTimeTool())
        self.register(AppLauncherTool())

    def register(self, tool):
        self.tools[tool.name] = tool

    def get_tool(self, name):
        return self.tools.get(name)

    def execute(self, tool_name, **kwargs):

        tool = self.get_tool(tool_name)

        if tool is None:
            return None

        return tool.execute(**kwargs)

    def get_function_schemas(self):

        return [
            tool.function_schema
            for tool in self.tools.values()
        ]
    
    def list_tools(self):
        return list(self.tools.values())