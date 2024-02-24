from kalkulacka import Pavel

def test_Pavel_increase():
    pavlicek = Pavel(5)
    expected = 6

    result = pavlicek.increase()

    assert result == expected