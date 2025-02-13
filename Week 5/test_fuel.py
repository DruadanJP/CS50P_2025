import pytest
from fuel import convert
from fuel import gauge


def test_valueerror():
    with pytest.raises(ValueError):
        convert("sd")
        convert("cat/dog")
        convert("s/50")
        convert("-5/10")
        convert("5/-3")
        convert("1.5/3")
        convert("10/3")
        convert("10/0")
        convert("10/")
        convert("/10")
        convert("10/10/10")
        convert("10.0/3")
        convert("3/10.0")
        convert("3/ 10")
        convert(" 3/10")
        convert("101/100")
        convert("100/101")


def test_zeroerror():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_fraction():
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
