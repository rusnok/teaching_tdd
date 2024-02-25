def odd_indexes(string):
    return str(string)[1::2]

def test_strings():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"

def test_integers():
    assert odd_indexes(3456) == "46"