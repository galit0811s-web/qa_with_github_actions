import pytest

from src.app import add_two_numbers


def test_add_two_numbers_positive_values():
    assert add_two_numbers(1, 2) == 3


def test_add_two_numbers_negative_values():
    assert add_two_numbers(-5, -10) == -15


def test_add_two_numbers_mixed_signs():
    assert add_two_numbers(-3, 7) == 4


def test_add_two_numbers_zero():
    assert add_two_numbers(0, 5) == 5


def test_add_two_numbers_large_values():
    assert add_two_numbers(1000000, 2500000) == 3500000
