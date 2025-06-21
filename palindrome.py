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
        value = value.lower()
        value = value.replace(" ","")
        d = deque()
        for x in value:
            d.append(x)
        e = deque(reversed(d))
        if d == e:
            return True
        if d != e:
            return False


is_Palindrome("Able was I ere I saw Elba")