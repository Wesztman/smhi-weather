import requests
import logging
import json

# Decorator which wraps the http request in a try/except
# block and validates the response for http errors
def _validate_response(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.error(err)
            raise
        return response

    return wrapper


class SmhiWeather:
    def __init__(self, latitude, longitude, api_version=2, http_timeout_in_seconds=30):
        self.latitude = latitude
        self.longitude = longitude
        self.api_version = api_version
        self.http_timeout_in_seconds = http_timeout_in_seconds

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value

    @property
    def api_version(self):
        return self._api_version

    @api_version.setter
    def api_version(self, value):
        if not isinstance(value, int):
            raise TypeError("API version must be an integer")
        if value < 1 or value > 2:
            raise ValueError("API version must be 1 or 2")
        self._api_version = value

    @property
    def http_timeout_in_seconds(self):
        return self._http_timeout_in_seconds

    @http_timeout_in_seconds.setter
    def http_timeout_in_seconds(self, value):
        if not isinstance(value, int):
            raise TypeError("HTTP timeout must be an integer")
        self._http_timeout_in_seconds = value

    @_validate_response
    def _get(self, url: str) -> requests.Response:
        logging.info("Sending GET request to %s", url)
        response = requests.get(url, timeout=self.http_timeout_in_seconds)
        return response

    def get_forecast(self, save_to_file: bool = False) -> dict:
        url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/{self.api_version}/geotype/point/lon/{self.longitude}/lat/{self.latitude}/data.json"
        response = self._get(url).json()
        logging.debug(json.dumps(response, indent=4))
        if save_to_file:
            with open("forecast.json", "w") as f:
                json.dump(response, f, indent=4)
        return response
