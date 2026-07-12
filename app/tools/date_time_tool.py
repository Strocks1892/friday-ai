from datetime import datetime

from app.tools.base_tool import BaseTool


class DateTimeTool(BaseTool):

    @property
    def name(self):
        return "datetime"

    @property
    def description(self):
        return "Returns the current date and time."
    
    @property
    def parameters(self):
        return {}

    def execute(self):

        now = datetime.now()

        return (
            f"Today's date is {now.strftime('%d %B %Y')}.\n"
            f"The current time is {now.strftime('%I:%M %p')}."
        )