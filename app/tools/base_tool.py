from abc import ABC, abstractmethod


class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self):
        """Tool name"""
        pass

    @property
    @abstractmethod
    def description(self):
        """Tool description"""
        pass

    @property
    @abstractmethod
    def parameters(self):
        """
        Gemini/OpenAI compatible parameter schema.
        """
        pass

    @property
    def function_schema(self):
        """
        Complete function definition used by AI models.
        """

        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self.parameters,
                "required": list(self.parameters.keys())
            }
        }

    @abstractmethod
    def execute(self, **kwargs):
        pass