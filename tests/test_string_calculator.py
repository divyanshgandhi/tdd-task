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

    def test_newline_separated_numbers_return_sum(self):
        """
        RED PHASE: Newline-separated numbers should return their sum
        Testing with "1\n2" should return 3
        """
        result = self.calculator.add("1\n2")
        assert result == 3

    def test_mixed_comma_and_newline_delimiters_return_sum(self):
        """
        RED PHASE: Mixed comma and newline delimiters should return sum
        Testing with "1\n2,3" should return 6
        """
        result = self.calculator.add("1\n2,3")
        assert result == 6

    def test_custom_delimiter_semicolon_return_sum(self):
        """
        RED PHASE: Custom semicolon delimiter should return sum
        Testing with "//;\n1;2" should return 3
        """
        result = self.calculator.add("//;\n1;2")
        assert result == 3

    def test_custom_delimiter_pipe_return_sum(self):
        """
        RED PHASE: Custom pipe delimiter should return sum
        Testing with "//|\n1|2|3" should return 6
        """
        result = self.calculator.add("//|\n1|2|3")
        assert result == 6

    def test_custom_delimiter_asterisk_return_sum(self):
        """
        RED PHASE: Custom asterisk delimiter should return sum
        Testing with "//*\n1*2*3*4" should return 10
        """
        result = self.calculator.add("//*\n1*2*3*4")
        assert result == 10

    def test_invalid_trailing_comma_newline_raises_error(self):
        """
        EDGE CASE: Invalid input "1,\n" should raise ValueError
        This input is NOT allowed as per kata requirements
        """
        with pytest.raises(ValueError):
            self.calculator.add("1,\n")

    def test_invalid_empty_parts_raise_error(self):
        """
        EDGE CASE: Empty parts in input should raise ValueError
        Testing various invalid formats with empty segments
        """
        with pytest.raises(ValueError):
            self.calculator.add("1,,2")  # Double comma
        
        with pytest.raises(ValueError):
            self.calculator.add("1,")    # Trailing comma
        
        with pytest.raises(ValueError):
            self.calculator.add(",1")    # Leading comma

    def test_single_negative_number_throws_exception(self):
        """
        RED PHASE: Single negative number should throw exception
        Testing with "1,-2,3" should raise ValueError with message
        """
        with pytest.raises(ValueError, match="negatives not allowed: -2"):
            self.calculator.add("1,-2,3")

    def test_multiple_negative_numbers_throw_exception(self):
        """
        RED PHASE: Multiple negative numbers should show all in exception
        Testing with "-1,-2,3" should raise ValueError with both negatives
        """
        with pytest.raises(ValueError, match="negatives not allowed: -1, -2"):
            self.calculator.add("-1,-2,3")

    def test_negative_with_custom_delimiter_throws_exception(self):
        """
        RED PHASE: Negative numbers with custom delimiters should throw exception
        Testing with "//;\n1;-2;3" should raise ValueError
        """
        with pytest.raises(ValueError, match="negatives not allowed: -2"):
            self.calculator.add("//;\n1;-2;3")

    def test_numbers_bigger_than_1000_are_ignored(self):
        """
        ADVANCED FEATURE: Numbers bigger than 1000 should be ignored
        Testing with "2,1001" should return 2 (1001 ignored)
        """
        result = self.calculator.add("2,1001")
        assert result == 2

    def test_multiple_numbers_over_1000_ignored(self):
        """
        ADVANCED FEATURE: Multiple numbers over 1000 should be ignored
        Testing with "1,2,1001,1002,3" should return 6 (1001,1002 ignored)
        """
        result = self.calculator.add("1,2,1001,1002,3")
        assert result == 6

    def test_exactly_1000_is_included(self):
        """
        ADVANCED FEATURE: Exactly 1000 should be included (boundary test)
        Testing with "2,1000" should return 1002
        """
        result = self.calculator.add("2,1000")
        assert result == 1002

    def test_long_delimiter_with_brackets(self):
        """
        ADVANCED FEATURE: Long delimiters with bracket notation
        Testing with "//[***]\n1***2***3" should return 6
        """
        result = self.calculator.add("//[***]\n1***2***3")
        assert result == 6

    def test_long_delimiter_different_pattern(self):
        """
        ADVANCED FEATURE: Different long delimiter pattern
        Testing with "//[sep]\n2sep3sep4" should return 9
        """
        result = self.calculator.add("//[sep]\n2sep3sep4")
        assert result == 9

    def test_long_delimiter_single_char_in_brackets(self):
        """
        ADVANCED FEATURE: Single char in brackets should work
        Testing with "//[;]\n1;2;3" should return 6
        """
        result = self.calculator.add("//[;]\n1;2;3")
        assert result == 6
