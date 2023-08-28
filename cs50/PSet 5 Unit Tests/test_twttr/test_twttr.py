from twttr import shorten

def test_twttr():
    assert shorten("Hello") == "Hll"
    assert shorten("Hi my name is 123") == "H my nm s 123"
    assert shorten("HELLO") == "HLL"