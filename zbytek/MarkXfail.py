import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.skip(reason="přeskočení tohoto testu")  # tento test se přeskočí
def test_aa(self):
    assert True

@pytest.mark.parametrize("x,y", [(0,2), (1,3)])
def test_foo_zip(x, y):
    pass

@pytest.mark.parametrize("x", [0, 1, 2])
@pytest.mark.parametrize("y", [2, 3, 6])
def test_foo_kazdy_s_kazdym(x, y):
    pass