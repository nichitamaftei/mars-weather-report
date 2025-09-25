from marsWeatherReport import jsonValidation
from jsonschema import ValidationError
import pytest

# ----------------------------
# HAPPY PATH: valid Json data
# ----------------------------

@pytest.mark.parametrize("goodJsonStructure")([
    {"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}}, # just one value
    {"671": {"AT": {"av": -54,"ct": 177556,"mn": -90,"mx": -2}}, "672": {"AT": {"av": -52,"ct": 177556,"mn": -93,"mx": -6}}},  # two values
])

def test_detailedSol_invalidJSONStructure_happy(goodJsonStructure):
    assert jsonValidation(goodJsonStructure) == goodJsonStructure


# ----------------------------
# Sad PATH: invalid json data
# ----------------------------
    
@pytest.mark.parametrize("badJsonStructure")([
    {},  # completely empty
    {"100": {}},  # "AT" missing
    {"100": {"AT": {"av": -20}}},  # "mn" and "mx" missing
    {"100": {"AT": {"av": "cold", "mn": -50, "mx": 5}}},  # wrong type
])
    
def test_detailedSol_invalidJSONStructure_sad(badJsonStructure):
    with pytest.raises(ValidationError) as exp:
        jsonValidation(badJsonStructure)
    assert str(exp.value) == "Invalid JSON structure"