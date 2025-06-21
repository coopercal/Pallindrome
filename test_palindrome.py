"""
Tests the palindrome module
"""
import pytest

from palindrome import is_Palindrome


def test_ValueError():
    with pytest.raises(ValueError):
        is_Palindrome(10)

def test_returnsFalseWithEmptyString():
    assert is_Palindrome("") == False

def test_returnsTrueWithA():
    assert is_Palindrome("a") == True

def test_returnsTrueWithBB():
    assert is_Palindrome("bb") == True

def test_returnsFalseWithABC():
    assert is_Palindrome("abc") == False

def test_returnsTrueWithLaval():
    assert is_Palindrome("laval") == True

def test_returnsFalseWithToronto():
    assert is_Palindrome("toronto") == False

def test_returnsTrueWithAble():
    assert is_Palindrome("Able was I ere I saw Elba") == True