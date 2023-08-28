import pytest
from seasons import calculate_age, convert_to_words

def test_calculate():
    assert calculate_age("2022-07-18") == 525600
    assert calculate_age("2021-07-18") == 1051200


def test_convert():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(100) == "One hundred"


def test_value_error():
    with pytest.raises(SystemExit):
        assert calculate_age("01.01.2000")