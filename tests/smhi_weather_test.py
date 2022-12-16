from smhi_weather import SmhiWeather
import pytest


class TestIntegrationSmhiWeather:
    """Tests which uses the real API"""

    def test_get_forecast(self):
        """Test that we can get a forecast"""
        smhi = SmhiWeather(59.334591, 18.063240)
        forecast = smhi.get_forecast()
        assert forecast is not None
        assert isinstance(forecast, dict)


class TestUnitSmhiWeather:
    """Tests which does not use the real API"""

    def test_get_forecast_with_invalid_api_version(self):
        """Test that we get an exception if we use an invalid API version"""
        with pytest.raises(ValueError):
            SmhiWeather(59.334591, 18.063240, api_version=3)

    def test_get_forecast_with_invalid_latitude(self):
        """Test that we get an exception if we use an invalid latitude"""
        with pytest.raises(ValueError):
            SmhiWeather(91.0, 18.063240)

    def test_get_forecast_with_invalid_longitude(self):
        """Test that we get an exception if we use an invalid longitude"""
        with pytest.raises(ValueError):
            SmhiWeather(59.334591, 181.0)

    def test_get_forecast_with_invalid_timeout(self):
        """Test that we get an exception if we use an invalid timeout"""
        with pytest.raises(TypeError):
            SmhiWeather(59.334591, 18.063240, http_timeout_in_seconds="30")

    def test_get_forecast_with_invalid_latitude_type(self):
        """Test that we get an exception if we use an invalid latitude type"""
        with pytest.raises(TypeError):
            SmhiWeather("59.334591", 18.063240)

    def test_get_forecast_with_invalid_longitude_type(self):
        """Test that we get an exception if we use an invalid longitude type"""
        with pytest.raises(TypeError):
            SmhiWeather(59.334591, "18.063240")

    def test_get_forecast_with_invalid_api_version_type(self):
        """Test that we get an exception if we use an invalid API version type"""
        with pytest.raises(TypeError):
            SmhiWeather(59.334591, 18.063240, api_version="1234")

    def test_get_forecast_with_invalid_timeout_type(self):
        """Test that we get an exception if we use an invalid timeout type"""
        with pytest.raises(TypeError):
            SmhiWeather(59.334591, 18.063240, http_timeout_in_seconds=30.0)
