# Aprendizaje de Maquina 1 (Machine Learning 1)

## Crime prediction in Buenos Aires based on weather data

This repo contiains the analysis and evaluation of different machine learning models to predict number of crimes in Buenos Aires for a given day, based on weather conditions.

In `TP.ipynb` you will find:

- Analysis of each dataset:
  -  [Historical weather data in Buenos Aires](https://open-meteo.com/en/docs/historical-weather-api#latitude=-34.6036&longitude=-58.3818&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,precipitation,rain,weather_code,pressure_msl,surface_pressure,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,wind_speed_10m,wind_direction_10m,wind_gusts_10m,is_day,sunshine_duration&daily=&timezone=auto)
  -  [Historical crime data in Buenos Aires](https://data.buenosaires.gob.ar/dataset/delitos)
- Creation of a joint dataset
- Analysis of variables and correlations between each other.
- Evaluation of different machine learning models:
   - Linear Regression
   - Ridge Regression
   - SVR
   - KNN
   - Decision Tree
   - Random Forest
   - AdaBoost
   - XGBoost
- Final results and conclusions
