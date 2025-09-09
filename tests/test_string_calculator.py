"""
Test cases for String Calculator TDD Kata

Following the Red-Green-Refactor cycle for each test case.
Each test represents a specific requirement from the kata.
"""

import pytest
from src.string_calculator import StringCalculator


class TestStringCalculator:
    """Test cases for the String Calculator implementation."""

    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """
        RED PHASE: First test - empty string should return 0
        This test will initially fail until we implement the add method.
        """
        result = self.calculator.add("")
        assert result == 0

    def test_single_number_returns_itself(self):
        """
        RED PHASE: Single number should return that number
        Testing with "1" should return 1
        """
        result = self.calculator.add("1")
        assert result == 1

    def test_two_comma_separated_numbers_return_sum(self):
        """
        RED PHASE: Two comma-separated numbers should return their sum
        Testing with "1,2" should return 3
        """
        result = self.calculator.add("1,2")
        assert result == 3

    def test_multiple_comma_separated_numbers_return_sum(self):
        """
        RED PHASE: Multiple comma-separated numbers should return their sum
        Testing with "1,2,3" should return 6
        """
        result = self.calculator.add("1,2,3")
        assert result == 6

    def test_many_comma_separated_numbers_return_sum(self):
        """
        RED PHASE: Many comma-separated numbers should return their sum
        Testing with "1,2,3,4,5" should return 15
        """
        result = self.calculator.add("1,2,3,4,5")
        assert result == 15
