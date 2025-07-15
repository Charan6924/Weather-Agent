from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
mcp = FastMCP("Weather-Agent")

def make_request(url : str) -> dict | None:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        return data

def format_data(data : dict) -> str:
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']
    clouds = data['clouds']['all']

    return (
    f"""Weather : {weather}.
    Temperature: {temp}°C (Feels like: {feels_like}°C).
    Humidity: {humidity}%. Pressure: {pressure} hPa.
    Wind: {wind_speed} m/s at {wind_deg}°.
    Cloudiness: {clouds}%."""
)

@mcp.tool()
def get_weather(city : str) -> str:
    """
        Fetches and returns the current weather information for the city entered.
    """
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    data = make_request(URL)

    out = format_data(data)

    return out

if __name__ == "__main__":
    print("MCP server is running...", flush=True)
    mcp.run(transport = "stdio")