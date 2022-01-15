from enum import Enum


class NumberEnum(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ZERO = "zero"


def check_number(number: int) -> NumberEnum:
    """
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
    else:
        return NumberEnum.ZERO.value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
