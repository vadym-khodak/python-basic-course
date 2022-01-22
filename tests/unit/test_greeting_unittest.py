"""
Запуск unittest: python -m unittest tests/unit/test_greeting_unittest.py -v
Запуск unittest для однієї тестової функції: python -m unittest tests/unit/test_greeting_unittest.py::test_greeting_with_name_check_title
Module unittest documentation: https://docs.pytest.org/en/6.2.x/contents.html
Video example: https://youtu.be/6tNS--WetLI
"""
from unittest import TestCase

from course.code.tests.hello import greeting


class TestGreeting(TestCase):
    def test_greeting_without_argument(self):
        result = greeting()
        self.assertEqual(result, "Hello World!")

    def test_greeting_with_name(self):
        result = greeting("Vadym")
        self.assertEqual(result, "Hello Vadym!")

    def test_greeting_with_name_check_title(self):
        result = greeting("vadYm")
        self.assertEqual(result, "Hello Vadym!")
