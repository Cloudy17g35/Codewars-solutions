"""
Write a function that returns only the decimal part of the given number.

You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.
"""


def get_decimal(n):
    return float('.' + str(n).split('.')[1]) if '.' in str(n) else 0
