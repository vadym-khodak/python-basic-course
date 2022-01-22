"""
Запуск doctest: python -m doctest course/code/tests/hello.py -v
Module Doctest documentation: https://docs.python.org/fr/3/library/doctest.html
"""


def greeting(name="World"):
    """
    >>> greeting()
    'Hello World!'
    >>> greeting("Vadym")
    'Hello Vadym!'
    >>> greeting("vadYm")
    'Hello Vadym!'
    """
    return f"Hello {name.title()}!"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
