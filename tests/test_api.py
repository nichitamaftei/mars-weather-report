from marsWeatherReport import getWeatherFromMars
import pytest
from unittest.mock import patch, Mock
import requests

# ----------------------------
# HAPPY PATH: valid day numbers
# ----------------------------

@patch("marsWeatherReport.api.requests.get")
def test_getWeatherFromMars_success(mock_get):
    # fake API response
    mock_response = {
        "1000": {
            "AT": 
                {"av": -54, 
                 "ct": 177556, 
                 "mn": -90, 
                 "mx": -2
                 }
            }
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    data = getWeatherFromMars()

    assert data != {}
    assert "1000" in data
    assert data["1000"]["AT"]["mn"] == -90

# ----------------------------
# SAD PATH: invalid inputs
# ----------------------------

@patch("marsWeatherReport.api.os.getenv")
def test_getWeatherFromMars_emptyAPI_failure(mock_getenv):
    
    # simulate missing API key
    mock_getenv.return_value = None

    with pytest.raises(ValueError) as exp:
        getWeatherFromMars()
    assert str(exp.value) == "API_KEY is missing, please add your NASA API key as an environment variable  or in a .env file"
    

@pytest.mark.parametrize("effect, expectedErrorMessage, statusCode",[
        (requests.exceptions.Timeout, "NASA API request timed out", None),
        (requests.exceptions.ConnectionError, "Failed to connect to NASA API", None),
        (requests.exceptions.RequestException, "Unexpected error: ", None),
        (None, "Invalid API key or forbidden access", 403),
        (None, "NASA API endpoint not found", 404),
        (None, "HTTP error 399", 399),
    ]
)
@patch("marsWeatherReport.api.requests.get")
def test_getWeatherFromMars_timeout_failure(mock_get, effect, expectedErrorMessage, statusCode):
    
    if effect is not None:
        mock_get.side_effect = effect
    else:
        mock_resp = Mock()
        mock_resp.status_code = statusCode
        mock_resp.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_resp)
        mock_get.return_value = mock_resp

    with pytest.raises(RuntimeError) as exp:
        data = getWeatherFromMars()
    assert str(exp.value) == expectedErrorMessage
    