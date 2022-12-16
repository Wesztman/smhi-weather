# smhi-weather

[![PyPI version](https://badge.fury.io/py/smhi-weather.svg)](https://badge.fury.io/py/smhi-weather)
[![Testing](https://github.com/Wesztman/smhi-weather/actions/workflows/testing.yml/badge.svg)](https://github.com/Wesztman/smhi-weather/actions/workflows/testing.yml)

Provides friendly functions to fetch data from SMHI:s open data api.

The source off all data provided is [SMHI](http://opendata.smhi.se/apidocs/metfcst/index.html),
use in accordance with SMHI:s guidelines and API policy.

Install with

`pip install smhi-weather`

Import and use as

```
from smhi_weather import SmhiWeather

forecast = SmhiWeather(59.334591, 18.063240).get_forecast()

print(forecast)
```

Forecast data can also be save to a file called `forecast.json` with

```
from smhi_weather import SmhiWeather

SmhiWeather(59.334591, 18.063240).get_forecast(save_to_file=True)
```

For now a single function exists which return a full forecast according to SMHI:s docs on [Get Point Forecast](http://opendata.smhi.se/apidocs/metfcst/get-forecast.html).
