class API:
    @classmethod
    def get_data(cls):
        return open('aa').readlines()

def get_only_numbers():
    numbers = []
    for line in API.get_data():
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        numbers.extend(digits)

    return '|'.join(numbers)

from unittest.mock import patch, MagicMock

def test_get_only_numbers():
    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]
    expected = "1|4|5|25|23|4|324|24|1|23|545|32"
    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  mockovani get_data metody
    with patch('MockingUnitTest.API', fake_api):
        # patch nahrazuje originální objekty a správce kontextu definuje rozsah použití mocku
        result = get_only_numbers()
        assert result == expected