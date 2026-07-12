import re

from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return "Performs mathematical calculations."
    
    @property
    def parameters(self):
        return {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate."
            }
        }

    def execute(self, expression: str):

        try:
            expression = re.sub(
                r"[^0-9+\-*/(). ]",
                "",
                expression
            )

            answer = eval(expression)

            return str(answer)

        except Exception:
            return "Invalid mathematical expression."