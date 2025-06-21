"""
Tests the palindrome module
"""
import pytest

from palindrome import is_Palindrome


def test_ValueError():
    with pytest.raises(ValueError):
        is_Palindrome(10)

def test_returnsFalseWithEmptyString():
    assert is_Palindrome("") == "False"

def test_returnsTrueWithA():
    assert is_Palindrome("a") == "True"