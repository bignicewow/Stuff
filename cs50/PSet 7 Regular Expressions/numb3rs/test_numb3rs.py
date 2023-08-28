from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True


def test_invalid_ip():
    assert validate("500.0.0.1") == False
    assert validate("cat") == False
    