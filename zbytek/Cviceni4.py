def _get_data(how_much):
    with open('test2.txt', 'r') as f:
        return f.read(how_much)

def get_avg(how_much):
    data = _get_data(how_much)
    numbers = [int(x) for x in data]
    return sum(numbers) / len(numbers)

from unittest.mock import patch, MagicMock

def test_get_avg():
    test_data = "123456789"
    expected = 45/9
    fake_get_data = MagicMock()
    fake_get_data.return_value = test_data
    with patch('Cviceni4._get_data', fake_get_data):
        result = get_avg("libovolne_how_much")
        assert result == expected

def test_func():
    _get_data_mock = MagicMock(return_value="123456789")
    with patch('Cviceni4._get_data', _get_data_mock):
        assert get_avg(3) == 2
        assert get_avg(1) == 1
        assert get_avg(2) == 1.5