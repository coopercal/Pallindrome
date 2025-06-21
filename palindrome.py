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
        d = deque()
        for x in value:
            d.append(x)
        print(d)
        e = deque(reversed(d))
        print(e)
        if d == e:
            print("true")
            return True
        if d != e:
            print("false")
            return False


is_Palindrome("Able was I ere I saw Elba")