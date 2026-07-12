from app.tools.tool_manager import ToolManager

tool_manager = ToolManager()


def calculate(expression: str) -> str:
    return tool_manager.execute(
        "calculator",
        expression=expression
    )


def get_datetime() -> str:
    return tool_manager.execute(
        "datetime"
    )


def open_application(app_name: str) -> str:
    return tool_manager.execute(
        "app_launcher",
        app_name=app_name
    )