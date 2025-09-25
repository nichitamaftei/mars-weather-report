from marsWeatherReport import day_with_suffix
import pytest

# ----------------------------
# HAPPY PATH: valid day numbers
# ----------------------------

@pytest.mark.parametrize("day_valid,expected_result", [
    (1, "1st"),
    (2, "2nd"),
    (3, "3rd"),
    (4, "4th"),
    (5, "5th"),
    (11, "11th"),
    (12, "12th"),
    (13, "13th"),
    (21, "21st")
])

def test_day_with_suffix_happy(day_valid, expected_result):
    assert day_with_suffix(day_valid) == expected_result
    
# ----------------------------
# SAD PATH: invalid inputs
# ----------------------------


@pytest.mark.parametrize("day_invalid, expected_error", [
    (0, "Day must be a positive integer and above 0"),
    (-1, "Day must be a positive integer and above 0"),
    (32, "Day must be less than or equal to 31"),
    ("1", "Day must be an integer")
])

def test_day_with_suffix_sad(day_invalid, expected_error):
    with pytest.raises(ValueError) as exp:
        day_with_suffix(day_invalid)
    assert str(exp.value) == expected_error
