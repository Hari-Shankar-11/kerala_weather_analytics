# Kerala Weather Forecast & Analysis
## Kannur vs Kozhikode | ETL Pipeline + ML Prediction


## Problem Statement
Weather forecasting is critical for daily life in Kerala — a state highly dependent on agriculture and tourism. Most people rely on generic national forecasts that don't capture city-level differences.

**This project answers:**
- How does weather differ between Kannur and Calicut?
- What will temperatures look like beyond the 5-day forecast window?
- Can we identify patterns in humidity and rainfall probability?


## 🏗️ Project Architecture

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

