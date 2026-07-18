from app.tools.tool_manager import ToolManager

tool_manager = ToolManager()


def search_web(query: str) -> str:
    """
    Search the web for up-to-date information.

    Args:
        query: The search query.
    """

    return tool_manager.execute(
        "browser_search",
        query=query
    )