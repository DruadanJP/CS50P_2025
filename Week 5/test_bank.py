from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("   Hello world  ") == 0  # Testing case insensitivity and spaces
    assert value("HELLO") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20
    assert value("  hmmm  ") == 20  # Ensure whitespace handling


def test_other():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("bye") == 100
    assert value("1234") == 100  # Edge case: no letters
