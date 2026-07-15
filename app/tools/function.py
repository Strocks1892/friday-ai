from app.tools.tool_manager import ToolManager

tool_manager = ToolManager()


def calculate(expression: str) -> str:
    """
    Perform mathematical calculations.

    Args:
        expression: Mathematical expression to evaluate.
    """
    return tool_manager.execute(
        "calculator",
        expression=expression
    )


def get_datetime() -> str:
    """
    Get the current local date and time.
    """
    return tool_manager.execute(
        "datetime"
    )


def open_application(app_name: str) -> str:
    """
    Open an application installed on the computer.

    Args:
        app_name: Name of the application to launch.
    """
    return tool_manager.execute(
        "app_launcher",
        app_name=app_name
    )