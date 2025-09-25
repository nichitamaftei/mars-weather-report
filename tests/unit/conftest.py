import pytest

# this is a sample valid incoming json structure
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