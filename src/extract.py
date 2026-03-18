import requests
import logging

logger = logging.getLogger(__name__)

def fetch_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},IN&appid={api_key}&units=metric"
    try:
        logger.info(f"Fetching forecast for {city}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logger.info(f"Success for {city}")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Failed for {city}: {e}")
        return None
