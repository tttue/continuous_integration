"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    """Test class
    """
    def test_addition(self):
        """test_addition
        """
        assert None == calculator.add(None, 2)
        assert None == calculator.add(2, None)
        assert None == calculator.add()
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """test_subtraction
        """
        assert 2 == calculator.subtract(4, 2)
