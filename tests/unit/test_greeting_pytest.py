"""
Запуск pytest: python -m pytest tests/unit/test_greeting_pytest.py -v
Запуск pytest однієї тестової функції: python -m pytest tests/unit/test_greeting_pytest.py::test_greeting_with_name_check_title
Library pytest documentation: https://docs.pytest.org/en/6.2.x/contents.html
"""
from course.code.tests.hello import greeting


def test_greeting_without_argument():
    result = greeting()
    assert result == "Hello World!"


def test_greeting_with_name():
    result = greeting("Vadym")
    assert result == "Hello Vadym!"


def test_greeting_with_name_check_title():
    result = greeting("vadYm")
    assert result == "Hello Vadym!"
