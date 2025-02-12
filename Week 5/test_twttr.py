from twttr import shorten


def test_default():
    assert shorten("Test") == "Tst"


def test_lowercase():
    assert shorten("test") == "tst"


def test_uppercase():
    assert shorten("TEST") == "TST"


def test_numbers():
    assert shorten("T3ST") == "T3ST"


def test_punct():
    assert shorten("TEST!") == "TST!"
