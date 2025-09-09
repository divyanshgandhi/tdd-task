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
