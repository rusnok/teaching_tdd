def prumer(seznam):
    return sum(seznam)/len(seznam)

def test_prumer():
    # Arange
    a = [1, 2, 3, 4, 5]
    expected = 3
    # Act
    result = prumer(a)
    # Assert
    assert expected == result

def test_prumer_karel():
    a = [5, 6, 7, 8, 9, 10]
    expected = 7.5
    result = sum(a) / len(a)

    assert result == expected