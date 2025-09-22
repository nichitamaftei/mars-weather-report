from marsWeatherReport import day_with_suffix
import pytest

def test_day_with_suffix_1():
    assert day_with_suffix(1) == "1st"

def test_day_with_suffix_2():
    assert day_with_suffix(2) == "2nd"

def test_day_with_suffix_3():
    assert day_with_suffix(3) == "3rd"
    
def test_day_with_suffix_4():
    assert day_with_suffix(4) == "4th"

def test_day_with_suffix_5():
    assert day_with_suffix(5) == "5th"
    
def test_day_with_suffix_6():
    assert day_with_suffix(11) == "11th"

def test_day_with_suffix_7():
    assert day_with_suffix(12) == "12th"

def test_day_with_suffix_8():
    assert day_with_suffix(13) == "13th"

def test_day_with_suffix_9():
    assert day_with_suffix(21) == "21st"

def test_day_with_suffix_10():
    with pytest.raises(ValueError) as exp:
        day_with_suffix(0)
    assert str(exp.value) == "Day must be a positive integer and above 0"

def test_day_with_suffix_11():
    with pytest.raises(ValueError) as exp:
        day_with_suffix(-1)
    assert str(exp.value) == "Day must be a positive integer and above 0"

def test_day_with_suffix_12():
    with pytest.raises(ValueError) as exp:
        day_with_suffix(32)
    assert str(exp.value) == "Day must be less than or equal to 31"

def test_day_with_suffix_13():
    with pytest.raises(ValueError) as exp:
        day_with_suffix("1")
    assert str(exp.value) == "Day must be an integer"