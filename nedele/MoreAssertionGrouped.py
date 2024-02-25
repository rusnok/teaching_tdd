import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_odd(self):
        pavel_si_vymyslel_novou_promennou = 2
        assert pavel_si_vymyslel_novou_promennou % 2 == 0, "hodnota byla licha, mela by byt suda"


class TestExceptionClass:
    def test_recursion_depth(self):
        with pytest.raises(RuntimeError) as vyjimka:
            def f():
                f()

            f()
        assert "maximum recursion" in str(vyjimka.value)
        assert vyjimka.type == RecursionError

    def test_foo_not_implemented(self):
        def foo():
            raise NotImplementedError

        with pytest.raises(RuntimeError) as excinfo:
            foo()
        assert excinfo.type is NotImplementedError

    def myfunc(self):
        raise ValueError("Exception 123 raised")

    def test_match(self):
        with pytest.raises(ValueError, match=r".* 123 .*"):
            self.myfunc()