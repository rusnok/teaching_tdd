from main import odd_indexes

def test_strings():
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"

def test_integers():
    assert odd_indexes(3456) == 46