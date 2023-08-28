import pytest
from working import convert

def test_pattern_one():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:00 AM to 7:00 PM") == "11:00 to 19:00"

def test_pattern_two():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 8 AM") == "00:00 to 08:00"

def test_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("11:30 PM to 7:30 AM") == "23:30 to 07:30"

def test_value_error():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")