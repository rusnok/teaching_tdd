def scitani(x, y):
    return x + y

import pytest

@pytest.fixture
def test_data():
    x = 2
    y = 3
    ocekavany_vysledek = 5
    return x, y, ocekavany_vysledek

def test_scitani(test_data):
    x, y, ocekavany_vysledek = test_data
    vysledek = scitani(x, y)
    assert vysledek == ocekavany_vysledek

# Pro predstavu co se plus minus deje v pozadi.
# data = test_data()
# test_scitani(test_data = data)