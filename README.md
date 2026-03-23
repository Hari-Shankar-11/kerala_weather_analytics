# Kerala Weather Forecast & Analysis
## Kannur vs Kozhikode | ETL Pipeline + ML Prediction


## Problem Statement
Kerala runs on the weather. Farmers plan their harvests around it. Tourists book their trips because of it. Fishermen stake their lives on it. Yet most weather apps serve up the same generic national forecast — one that completely misses the differences between two cities just 90 kilometres apart.
This project sets out to fix that, at least for Kannur and Kozhikode.

## What this project does:
It pulls live 5-day forecast data straight from the OpenWeatherMap API, cleans and structures it through an ETL pipeline, stores it in a local SQLite database, and then visualises exactly how the two cities differ — in temperature, humidity, and sky conditions. And when the API's 5-day window runs out? A Linear Regression model takes over and extends the temperature predictions by another 14 days.

**This project answers:**
- How does weather differ between Kannur and Calicut?
- What will temperatures look like beyond the 5-day forecast window?
- Can we identify patterns in humidity and rainfall probability?

## How It Works
The pipeline follows a simple ETL flow. First, it fetches the raw forecast JSON for each city. Then it parses out only the fields that matter — temperature, humidity, pressure, wind speed, and weather condition — into a clean pandas DataFrame. That data gets loaded into SQLite so it can be queried reliably, and then a series of Matplotlib and Seaborn charts bring the comparison to life.
For the machine learning step, Linear Regression is trained on the 40 forecast time steps per city and then projected forward by 56 more steps, giving a rough but useful view of where temperatures are headed.

##  Project Architecture

```
OpenWeatherMap API
↓
src/extract.py ← Fetch live forecast data
↓
src/transform.py ← Clean and structure data
↓
src/load.py ← Store in SQLite database
↓
outputs/ ← Charts and visualisations
```

## Features

- ✅ Live data ingestion from OpenWeatherMap API (5-day / 3-hour forecast)
- ✅ Automated ETL pipeline with structured logging
- ✅ SQLite storage for reproducible querying and analysis
- ✅ City-level comparison of temperature, humidity, and weather conditions
- ✅ ML-powered temperature predictions beyond the API's 5-day limit
- ✅ Charts exported as PNG files for reporting
  
##  How to Run

```bash
-git clone https://github.com/Hari-Shankar-11/kerala_weather_analytics
-ip install -r requirements.txt
-export OPENWEATHER_API_KEY="your_key_here"
-jupyter notebook weather_forecast.ipynb
```

|Library |Purpose |

```
|`requests` |Fetch data from OpenWeatherMap API |
|`pandas` |Data manipulation and transformation|
|`sqlite3` |Store structured data in database |
|`matplotlib` |Create visualisations |
|`seaborn` |Statistical charts |
|`scikit-learn`|Linear Regression ML model |
|`numpy` |Numerical computations |
|`logging` |Monitor pipeline health |
```


|Insight |Detail |
```
|Temperature range|23°C (night) to 30°C (afternoon) |
|Humidity |52% to 87% |
|Clear sky |Kannur 82.5% — Kozhikode 77.5% |
|Rain probability |12.5% for both cities |
|Temperature trend|Rising toward 31°C by early April|
```

 Machine Learning
 ```
Applied Linear Regression to extend temperature predictions beyond the 5-day API forecast window.
∙ Training data: 40 forecast points per city
∙ Prediction window: 14 days beyond forecast
∙ Limitation: Captures trend but not daily cycles
∙ Future improvement: SARIMA or Facebook Prophet
```

