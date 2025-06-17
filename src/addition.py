# app.py
# This is a test commit for addition of 2 numbers
# This is a test commit for addition of 2 positive & 2 negative number
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
