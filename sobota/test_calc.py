from kalkulacka import Calc

def test_init():
    c = Calc(1000, 2000)
    assert c.a == 1000
    assert c.b == 2000

def test_add():
    c = Calc(5, 3)
    result = c.add()
    expected = 8

    assert result == expected
    assert Calc(5, 3).add() == 8
    assert Calc(5, 0).add() == 5
    assert Calc(5, -3).add() == 2

def test_sub():
    c = Calc(5, 3)
    assert c.sub() == 2
    assert c.sub(True) == -2

def test_mul():
    c = Calc(5, 3)
    assert c.mul() == 15

def test_div():
    c = Calc(4, 2)
    assert c.div() == 2
    assert c.div(True) == 1/2

    d = Calc(1, 3)
    assert round(d.div(), 3) == round(1/3, 3)
