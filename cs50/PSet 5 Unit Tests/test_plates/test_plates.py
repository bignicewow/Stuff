from plates import is_valid, start_with_letters, min_and_max, check_for_number, only_alnum

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_start_with_letters():
    assert start_with_letters("CS50") == True
    assert start_with_letters("50CS") == False


def test_min_and_max():
    assert min_and_max("CS50") == True
    assert min_and_max("H") == False
    assert min_and_max("HELLOOO") == False


def test_check_for_number():
    assert check_for_number("CS50") == True
    assert check_for_number("CS05") == False
    assert check_for_number("AAA222") == True
    assert check_for_number("AA222A") == False


def test_only_alnum():
    assert only_alnum("CS50") == True
    assert only_alnum("PI3.14") == False
    assert only_alnum("CS./50") == False