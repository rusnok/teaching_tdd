from main import add_numbers

def test_add_numbers():
    a = 4
    b = 7
    expected = 11

    assert add_numbers(a, b) == expected


def test_add_numbers_with_negative_values():
    a = -20
    b = 3
    expected = -17

    assert add_numbers(a, b) == expected