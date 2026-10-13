# Unit test using pytest library
# pytest unit_test.py
import pytest

def addition(a, b):
    return a + b

def test_addition():
    assert addition(10, 20) == 30  # is addition function works properly on postive number or not.
    assert addition(-10, -10) == -20  # negative number test
    assert addition(-10, 30) == 20     # negative  and positive number test
    
def test_addition2():
    assert addition(0, 0) == 0  # zero test
    assert addition(100000000, -100000000) == 0  # positive and negative number test
    assert addition(1.5, 2.5) == 4.0  # float number test
    assert addition(1e10, 1e10) == 2e10  # large number test