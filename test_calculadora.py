from calculadora import soma, subtrai, multiplica, divide


def test_soma():
    assert soma(2, 3) == 5


def test_subtrai():
    assert subtrai(10, 4) == 6


def test_multiplica():
    assert multiplica(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_por_zero():
    assert divide(5, 0) is None
