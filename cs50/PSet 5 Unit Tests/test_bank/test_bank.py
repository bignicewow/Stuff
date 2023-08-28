from bank import value

def test_hello():
    assert value("Hello".lower()) == 0


def test_h():
    assert value("Hi!".lower()) == 20


def test_anything():
    assert value("Nice to meet you".lower()) == 100