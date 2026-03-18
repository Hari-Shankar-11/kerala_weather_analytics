import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_forecast(raw, city):
    df = pd.DataFrame([{
        "city": city,
        "datetime": item["dt_txt"],
        "temperature": item["main"]["temp"],
        "feels_like": item["main"]["feels_like"],
        "humidity": item["main"]["humidity"],
        "pressure": item["main"]["pressure"],
        "wind_speed": item["wind"]["speed"],
        "weather": item["weather"][0]["main"],
        "description": item["weather"][0]["description"],
    } for item in raw["list"]])

    df["datetime"] = pd.to_datetime(df["datetime"])
    logger.info(f"Transformed {len(df)} records for {city}")
    return df


def combine_cities(raw_data, cities):
    dfs = [transform_forecast(raw_data[city], city) for city in cities]
    df_all = pd.concat(dfs, ignore_index=True)
    logger.info(f"Combined dataset: {len(df_all)} total records")
    return df_all
