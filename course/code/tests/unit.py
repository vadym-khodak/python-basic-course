import random
from unittest import TestCase, mock

import pytest

from .main import check_number


def test_check_number_positive():
    # GIVEN a positive number
    num = random.randint(1, 100000000)
    # WHEN call `check_number` function with the positive number
    result = check_number(num)
    # THEN the result equals "positive"
    assert result == "positive"


def test_check_number_negative():
    # GIVEN a negative number
    num = random.randint(-100000000, 0)
    # WHEN call `check_number` function with the negative number
    result = check_number(num)
    # THEN the result equals "negative"
    assert result == "negative"


def test_check_number_zero():
    # GIVEN a zero number
    num = 0
    # WHEN call `check_number` function with zero number
    result = check_number(num)
    # THEN the result equals "zero"
    assert result == "zero", "Result is not 'zero'"


@pytest.mark.parametrize(
    "num,expected_value",
    [
        (1, "positive"),
        (-1, "negative"),
        (0, "zero"),
    ]
)
def test_check_number_all(num, expected_value):
    # GIVEN a positive number
    # num = random.randint(1, 10000000)
    # WHEN call `check_number` function with the positive number
    with mock.patch("main.random.randint") as mocked_random:
        result = check_number(num)
        assert mocked_random.called
        assert mocked_random.call_count == 2
    # THEN the result equals "positive"
    assert result == expected_value


class TestCheckNumber(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.positive = random.randint(1, 10000000)
        with open("../test.txt", "w") as f:
            f.write(f"Prepared data for testing {cls.positive}")

    @classmethod
    def tearDownClass(cls) -> None:
        """This function will be run before before all test methods"""
        del cls.positive
        with open("../test.txt", "w") as f:
            f.write("Deleted data for testing")

    def setUp(self) -> None:
        """This function will be run before each all test methods"""

    def tearDown(self) -> None:
        """This function will be run after each test method"""

    def test_check_number_positive(self):
        # GIVEN a positive number
        num = self.positive
        # WHEN call `check_number` function with the positive number
        result = check_number(num)
        # THEN the result equals "positive"
        self.assertEqual(result, "positive", "Result is not positive")

    def test_check_number_negative(self):
        # GIVEN a negative number
        num = random.randint(-100000000, 0)
        # WHEN call `check_number` function with the negative number
        result = check_number(num)
        # THEN the result equals "negative"
        self.assertEqual(result, "negative")

    def test_check_number_zero(self):
        # GIVEN a zero number
        num = 0
        # WHEN call `check_number` function with zero number
        result = check_number(num)
        # THEN the result equals "zero"
        self.assertEqual(result, "zero")
