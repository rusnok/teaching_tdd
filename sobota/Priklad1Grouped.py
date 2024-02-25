from main import sum_args

def sum_args(max_value, *args):
    soucet = 0
    max_value = max_value if isinstance(max_value, int) else 100
    for a in args:
        if isinstance(a, int) and a < max_value:
            soucet += a
    return soucet

class TestNormal:
    def test_sum_of_elements_below_max_val(self):
        max_value = 10
        elements = [2, 4, 5, 3, 9, 1, 0, -2]
        expected = 22
        assert sum_args(max_value, *elements) == expected


    def test_sum_of_elements_above_max_val(self):
        max_value = 8
        elements = [2, 4, 5, 3, 9, 1, 0, -2]
        expected = 13
        assert sum_args(max_value, *elements) == expected


class TestUndefined:
    def test_sum_of_elements_with_mixed_types(self):
        max_value = 8
        elements = [2, 4, 5, 3, 'test']

        expected = 14

        assert sum_args(max_value, *elements) == expected


    def test_sum_of_elements_with_invalid_max_val(self):
        max_value = 'test'
        elements = [2, 4, 5, 3]

        expected = 14

        assert sum_args(max_value, *elements) == expected


    def test_sum_of_elements_with_invalid_max_val_and_mixed_types(self):
        max_value = 'test'
        elements = [2, 4, 5, 3, 'test']

        expected = 14

        assert sum_args(max_value, *elements) == expected
