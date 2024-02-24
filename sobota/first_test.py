def add_numbers(a: int, b: int):
    return a + b

def test_add_numbers():
    # Setup
    a = 4
    b = 7
    expected = 11
    # Act
    result = add_numbers(a, b)

    # Assert
    assert result == expected


def test_add_numbers_with_negative_values():
    a = -20
    b = 3
    expected = -17

    assert add_numbers(a, b) == expected