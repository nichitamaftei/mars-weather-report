from marsWeatherReport import getWeatherFromMars, jsonValidation, detailedSol, plottingTemps
import pytest
import matplotlib
from unittest.mock import patch, Mock
import requests

# ----------------------------
# HAPPY PATH: valid workflow
# ----------------------------

@patch("marsWeatherReport.api.os.getenv")
@patch("marsWeatherReport.api.requests.get")
@patch("matplotlib.pyplot.show")
@pytest.mark.parametrize("goodJsonStructure, selectedSol", [
    ({"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}, "sol_keys": ["671"]}, "671"), # just one value
    ({"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}, "672": {"AT": {"av": -52,"ct": 177556,"mn": -93,"mx": -6}}, "sol_keys": ["671", "672"]}, "671")  # two values
])
def test_integration_end_to_end_solDetail_happy(mock_show, mock_get, mock_getenv, goodJsonStructure, selectedSol, capsys):
    
    # provide a fake API key
    mock_getenv.return_value = "fake_key"
    
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json = Mock(return_value=goodJsonStructure)
    mock_get.return_value = mock_resp
    
    data = getWeatherFromMars()
    
    validatedData = jsonValidation(data)
    
    av = goodJsonStructure[selectedSol]["AT"]["av"]
    mn = goodJsonStructure[selectedSol]["AT"]["mn"]
    mx = goodJsonStructure[selectedSol]["AT"]["mx"]
    
    detailedSol(validatedData, selectedSol)
    
    captured = capsys.readouterr()
    
    assert f"SOL {selectedSol} was chosen." in captured.out
    assert f"Average temperature: {av}°C" in captured.out
    assert f"Lowest temperature recorded: {mn}°C" in captured.out
    assert f"Highest temperature recorded: {mx}°C" in captured.out
    
@patch("marsWeatherReport.api.os.getenv")
@patch("matplotlib.pyplot.show")
@patch("marsWeatherReport.api.requests.get")
@pytest.mark.parametrize("goodJsonStructure", [
    {"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}, "sol_keys": ["671"]},
    {"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}, "672": {"AT": {"av": -52,"ct": 177556,"mn": -93,"mx": -6}}, "sol_keys": ["671", "672"]}
])
def test_integration_end_to_end_graph_happy(mock_get, mock_show, mock_getenv, goodJsonStructure):
    
    # provide a fake API key
    mock_getenv.return_value = "fake_key"
    
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json = Mock(return_value=goodJsonStructure)
    mock_get.return_value = mock_resp

    data = getWeatherFromMars()
    validatedData = jsonValidation(data)

    availableSols = validatedData["sol_keys"]
    fig = plottingTemps(validatedData, availableSols)

    assert data == goodJsonStructure
    assert isinstance(fig, matplotlib.figure.Figure)
    mock_show.assert_called_once()
