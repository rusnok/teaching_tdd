import pytest


class Ovoce:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.nakrajene_na_kosticky = False

    def nakrajet(self):
        self.nakrajene_na_kosticky = True


class OvocnySalat:
    def __init__(self, *misa_ovoce):
        self.ovoce_tuple = misa_ovoce
        self._nakrajej_ovoce()

    def _nakrajej_ovoce(self):
        for ovoce in self.ovoce_tuple:
            ovoce.nakrajet()


# Arrange
@pytest.fixture
def misa_ovoce():
    return [Ovoce("jablko"), Ovoce("banan")]


def test_fruit_salad(misa_ovoce):
    # Act
    ovocny_salat = OvocnySalat(*misa_ovoce)

    # Assert
    assert all(ovoce.nakrajene_na_kosticky for ovoce in ovocny_salat.ovoce_tuple)