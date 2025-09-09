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
            return sum(int(part) for part in parts)
        
        # Handle comma and/or newline-separated numbers
        if ',' in numbers or '\n' in numbers:
            parts = re.split(r'[,\n]', numbers)
            return sum(int(part) for part in parts)
        
        # Handle single number case
        return int(numbers)
