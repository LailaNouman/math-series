import pytest
from series import fibonacci
from series import lucas
from series import sum_series

# Fibonacci test
def test_zero_fibonacci():
    actual = fibonacci(0)
    expected = 0

    assert actual == expected

def test_one_fibonacci():
    actual = fibonacci(1)
    expected = 1

    assert actual == expected


def test_five_fibonacci():
    actual = fibonacci(5)
    expected = 5

    assert actual == expected

# Lucas tests
def test_zero_lucas():
    actual = lucas(0)
    expected = 2

    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 1

    assert actual == expected

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_five_lucas():
    actual = lucas(5)
    expected = 11

    assert actual == expected

# Sum tests
def test_sum_series_seven():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

def test_sum_series_four():
    actual = sum_series(4,2,3)
    expected = 13
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0,7,8)
    expected = 7
    assert actual == expected