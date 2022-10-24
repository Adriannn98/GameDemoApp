def add(a, b):
    return a + b


# assert add(2, 2) == 4
# assert add(2, 3) == 5
# assert add(2, 4) == 6
# assert add(2, 5) == 7
# assert add(0, 0) == 0
# assert add(1, 10) == 11
# assert add(10, 1) == 11
# assert add(1, 1) == 2
# assert add(-1, 11) == 10
# assert add(-1, -1) == -2

def test_add_01():
    assert add(2, 2) == 4

def test_add_02():
    assert add(2, 3) == 5

def test_add_03():
    assert add(2, 4) == 6

def test_add_04():
    assert add(2, 5) == 7