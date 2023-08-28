from um import count

def test_um():
    assert count("Um") == 1
    assert count("Um, um. Um?") == 3
    assert count(" um ") == 1


def test_no_um():
    assert count("Foobar") == 0
    assert count("Umbral") == 0
    assert count("Humor") == 0
    assert count("Hummus") == 0


def test_just_numbers():
    assert count("12345") == 0