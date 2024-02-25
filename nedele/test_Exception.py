import pytest
def capital_case(x):
    if isinstance(x, int):
        raise TypeError("Integer is wrong type")
    return x.capitalize()

def test_capital_case():
    assert capital_case('software') == 'Software'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError) as vyjimka:
        capital_case(9)
    assert "wrong type" in str(vyjimka.value)

def test_recursion_depth():
    with pytest.raises(RuntimeError) as vyjimka:
        def f():
            f()

        f()
    assert "maximum recursion" in str(vyjimka.value)
    assert vyjimka.type == RecursionError