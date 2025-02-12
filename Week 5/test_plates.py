from plates import is_valid


def test_fullstrings():
    assert is_valid("AAAAAA") == True


def test_fullint():
    assert is_valid("333333") != True


def test_endint():
    assert is_valid("AAAA33") == True


def test_middleint():
    assert is_valid("AA33AA") != True

def test_lenght():
    assert is_valid("A") != True

def test_alpha():
    assert is_valid("AA1") == True
    assert is_valid("AA#1") == False
    
def test_zero():
    assert is_valid("AA0333") == False