import pytest

def test_one():
    x = "this"
    assert "h" in x

def test_two():
    x = "hello"
    assert hasattr(x, "check")

def test_sudy():
    pavel_si_vymyslel_novou_promennou = 2
    assert pavel_si_vymyslel_novou_promennou % 2 == 0, "hodnota byla licha, mela by byt suda"


def test_recursion_depth():
    with pytest.raises(RuntimeError) as vyjimka:
        def f():
            f()

        f()
    assert "maximum recursion" in str(vyjimka.value)
    assert vyjimka.type == RecursionError

def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(Exception) as excinfo:
        foo()
    assert excinfo.type is NotImplementedError

def myfunc():
    raise ValueError("Pavel 123 ")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()