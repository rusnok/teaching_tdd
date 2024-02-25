import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("test_input", [8, 6, 42])
def test_deleni_dvema(test_input):
    assert test_input % 2 == 0