"""
This is at test file
Запуск doctest: python -m doctest course/code/tests/main.py -v
Module Doctest documentation: https://docs.python.org/fr/3/library/doctest.html
"""
from enum import Enum


class NumberEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ZERO = "zero"


def check_number(number: int) -> NumberEnum:
    """
    This a function to check whether this number is a positive number or not.

    >>> check_number(1)
    'positive'
    >>> check_number(-1)
    'negative'
    >>> check_number(0)
    'zero'
    """
    if number > 0:
        return NumberEnum.POSITIVE.value
    if number < 0:
        return NumberEnum.NEGATIVE.value
    return NumberEnum.ZERO.value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
