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
        d = deque()
        for x in value:
            d.append(x)
        e = deque(reversed(d))
        if d == e:
            print("true")
            return True
        if d != e:
            print("false")
            return False


is_Palindrome("abc")