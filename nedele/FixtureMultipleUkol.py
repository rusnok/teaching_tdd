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
    a, b, c_ocekavany_vysledek = test_data
    vysledek = scitani(a, b)
    assert vysledek == c_ocekavany_vysledek

@pytest.fixture
def x():
    return 2

@pytest.fixture
def y():
    return 3

@pytest.fixture
def ocekavany_vysledek():
    return 5

def test_scitani_multiple(x, y, ocekavany_vysledek):
    vysledek = scitani(x, y)
    assert vysledek == ocekavany_vysledek
