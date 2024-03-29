
from main import capital_case
import pytest


def test_capital_case():
    assert capital_case('software') == 'Software'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)