"""
Validates strings as palindromes.
"""
def is_Palindrome(value):
    if not isinstance(value, str):
        raise ValueError
    if value == "":
        print("False")

is_Palindrome("")