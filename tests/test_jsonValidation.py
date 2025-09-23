from marsWeatherReport import jsonValidation
from jsonschema import ValidationError
import pytest

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