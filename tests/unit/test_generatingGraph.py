from marsWeatherReport import plottingTemps
from unittest.mock import patch
from tests.conftest import jsonSampleData
import matplotlib
import pytest
import tempfile
import os

# ----------------------------
# Happy PATH: invalid json data
# ----------------------------

matplotlib.rcParams['savefig.directory'] = '/tmp'
os.environ['MPLCONFIGDIR'] = '/tmp'  # for font cache

@patch("matplotlib.pyplot.show")
def test_generatingGraph_happy(mock_show):
    
    fig = plottingTemps(jsonSampleData("2", -54, -92, 2), ["2"])
    fig.savefig(os.path.join(tempfile.gettempdir(), "mars_weather_plot.png"))
    
    mock_show.assert_called_once()
    assert isinstance(fig, matplotlib.figure.Figure)


# ----------------------------
# Sad PATH: empty data
# ----------------------------

@pytest.mark.parametrize("emptyData, emptyAvailableSols, expectedExceptionMsg", [
    ({}, [], "There are no available sols and data to plot"),
    (jsonSampleData("2", -54, -92, 2), [], "There are no available sols to plot"),
    ({}, ["1", "2", "3", "4"], "There is no available data to plot with")])


def test_generatingGraph_emptyInputs_sad(emptyData, emptyAvailableSols, expectedExceptionMsg):
    with pytest.raises(KeyError) as exp:
        plottingTemps(emptyData, emptyAvailableSols)
    assert str(exp.value).strip("'") == expectedExceptionMsg