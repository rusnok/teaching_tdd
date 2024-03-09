def scitani(x, y):
    return x + y

import pytest

@pytest.fixture
def test_data():
    x = 2
    y = 3
    ocekavany_vysledek = 5
    return x, y, ocekavany_vysledek

@pytest.fixture
def test_data_simple():
    return 10

def test_scitani(test_data):
    a, b, c_ocekavany_vysledek = test_data
    vysledek = scitani(a, b)
    assert vysledek == c_ocekavany_vysledek

def test_komutativita(test_data):
    x, y, ocekavany_vysledek = test_data
    vysledek = scitani(y, x)
    assert vysledek == ocekavany_vysledek

def test_simple(test_data_simple):
    assert 10 == test_data_simple

# Pro predstavu co se plus minus deje v pozadi.
# data = test_data()
# test_scitani(test_data = data)