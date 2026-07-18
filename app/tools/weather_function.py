from app.tools.tool_manager import ToolManager

tool_manager = ToolManager()


def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Args:
        city: Name of the city.
    """

    return tool_manager.execute(
        "weather",
        city=city
    )