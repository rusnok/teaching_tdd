def odd_indexes(string):
    return str(string)[1::2]

def test_strings():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"

def test_integers():
    assert odd_indexes(3456) == "46"

@pytest.mark.parametrize("test_input,expected",
                         [("elephant", "lpat"), ("computer", "optr"), (3456, "46")])
def test_str_and_int(test_input, expected):
    assert odd_indexes(test_input) == expected