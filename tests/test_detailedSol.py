from marsWeatherReport import detailedSol
import pytest

# this is a sample incoming json structure 
def jsonSampleData(sol, av, mn, mx):
    return {
        sol: {
            "AT": {
                "av": av,
                "ct": 177556,
                "mn": mn,
                "mx": mx
            }
        }
    }
    
# ----------------------------
# HAPPY PATH: valid Json data
# ----------------------------

# runs the same test with multiple inputs
@pytest.mark.parametrize("sol, av, mn, mx", [
    (678, -16, -98, -2),
    (621, -32, -102, -3),
    (612, -43, -23, -98),
])

def test_detailedSol_happy(sol, av, mn, mx, capsys):
    data = jsonSampleData(sol, av, mn, mx)
    
    detailedSol(data, sol)
    
    captured = capsys.readouterr()
    
    assert f"SOL {sol} was chosen." in captured.out
    assert f"Average temperature: {av}°C" in captured.out
    assert f"Lowest temperature recorded: {mn}°C" in captured.out
    assert f"Highest temperature recorded: {mx}°C" in captured.out
    
    
# ----------------------------
# Sad PATH: invalid json data
# ----------------------------
    
def test_detailedSol_mismatchSolKey_sad():
    with pytest.raises(KeyError) as exp:
        detailedSol(jsonSampleData(18, -32, -97, -4), 19)
    assert str(exp.value).strip("'") == "Sol not found in the Data"