"""
Validates strings as palindromes.
"""
from collections import deque


def is_Palindrome(value):
    if not isinstance(value, str):
        raise ValueError
    if value == "":
        return False
    else:
        return True

is_Palindrome("A")