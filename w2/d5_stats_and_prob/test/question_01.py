"""
Create a function that returns the mean of all digits.

Example:
    mean(42) ➞ 3.0

    mean(12345) ➞ 3.0

    mean(666) ➞ 6.0

Notes:
    - Function should always return float
"""


def mean(digits):
    str_digits = str(digits)
    split_digits = []
    for dgt in str_digits:
        int_dgt = int(dgt)
        split_digits.append(int_dgt)
    return(sum(split_digits)/ len(split_digits))