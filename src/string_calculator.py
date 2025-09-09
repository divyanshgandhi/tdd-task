"""
String Calculator implementation following TDD principles.

This class implements a calculator that can parse and sum numbers
from string input with various delimiters and rules.
"""

from typing import List
import re


class StringCalculator:
    """A calculator that processes comma-separated string numbers."""

    def add(self, numbers: str) -> int:
        """
        Calculate the sum of numbers in a string.
        
        Args:
            numbers: A string containing numbers separated by delimiters
            
        Returns:
            int: The sum of all numbers in the string
            
        Raises:
            ValueError: When negative numbers are provided
        """
        # Handle empty string case - minimal implementation
        if not numbers:
            return 0
        
        # Handle custom delimiter format: //[delimiter]\n[numbers...]
        if numbers.startswith('//'):
            # Extract custom delimiter and numbers
            delimiter_line, numbers_part = numbers.split('\n', 1)
            custom_delimiter = delimiter_line[2:]  # Remove '//' prefix
            # Escape special regex characters
            escaped_delimiter = re.escape(custom_delimiter)
            parts = re.split(escaped_delimiter, numbers_part)
            return self._calculate_sum_with_validation(parts)
        
        # Handle comma and/or newline-separated numbers
        if ',' in numbers or '\n' in numbers:
            parts = re.split(r'[,\n]', numbers)
            return self._calculate_sum_with_validation(parts)
        
        # Handle single number case
        number = int(numbers)
        if number < 0:
            raise ValueError(f"negatives not allowed: {number}")
        # Ignore numbers bigger than 1000
        if number > 1000:
            return 0
        return number

    def _calculate_sum_with_validation(self, parts: List[str]) -> int:
        """
        Calculate sum of string parts while validating for negative numbers.
        Numbers bigger than 1000 are ignored.
        
        Args:
            parts: List of string numbers to sum
            
        Returns:
            int: Sum of all valid positive numbers <= 1000
            
        Raises:
            ValueError: When negative numbers are found
        """
        numbers = [int(part) for part in parts]
        negatives = [num for num in numbers if num < 0]
        
        if negatives:
            negatives_str = ", ".join(str(neg) for neg in negatives)
            raise ValueError(f"negatives not allowed: {negatives_str}")
        
        # Filter out numbers bigger than 1000
        valid_numbers = [num for num in numbers if num <= 1000]
        return sum(valid_numbers)
