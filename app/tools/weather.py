import requests

from app.tools.base_tool import BaseTool


class WeatherTool(BaseTool):

    @property
    def name(self):
        return "weather"

    @property
    def description(self):
        return "Get the current weather for a city."

    @property
    def parameters(self):
        return {
            "city": {
                "type": "string",
                "description": "Name of the city."
            }
        }

    def execute(self, city: str):

        try:

            # Geocoding API
            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search"
                f"?name={city}&count=1"
            )

            geo = requests.get(geo_url).json()

            if "results" not in geo:
                return f"Sorry, I couldn't find the city '{city}'."

            location = geo["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            # Weather API
            weather_url = (
                "https://api.open-meteo.com/v1/forecast"
                f"?latitude={latitude}"
                f"&longitude={longitude}"
                "&current=temperature_2m,wind_speed_10m"
            )

            weather = requests.get(weather_url).json()

            current = weather["current"]

            return (
                f"Location: {location['name']}\n"
                f"Temperature: {current['temperature_2m']}°C\n"
                f"Wind Speed: {current['wind_speed_10m']} km/h"
            )

        except Exception as e:
            return f"Weather error: {e}"