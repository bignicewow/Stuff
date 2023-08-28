from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/1") == 100


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"