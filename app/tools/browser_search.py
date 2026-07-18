from ddgs import DDGS

from app.tools.base_tool import BaseTool


class BrowserSearchTool(BaseTool):

    @property
    def name(self):
        return "browser_search"

    @property
    def description(self):
        return "Search the web for up-to-date information."

    @property
    def parameters(self):
        return {
            "query": {
                "type": "string",
                "description": "The search query."
            }
        }

    def execute(self, query: str):
        print(f"🔍 Browser Search Tool called with query: {query}")

        try:

            with DDGS() as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

            if not results:
                return "No search results found."

            response = ""

            for i, result in enumerate(results, start=1):

                response += (
                    f"{i}. {result['title']}\n"
                    f"{result['body']}\n"
                    f"{result['href']}\n\n"
                )

            return response

        except Exception as e:
            return f"Search error: {e}"