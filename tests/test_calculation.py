"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.

def test_calculation_operations(arga, argb, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(arga, argb, operation)  # Create a Calculation instance with the provided operands and operation.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {arga} and {argb}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.
