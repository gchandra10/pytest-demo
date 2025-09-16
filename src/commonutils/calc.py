def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference between two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The difference between a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of two numbers. If the divisor is zero, return 'None' and print an error message.
    
    Parameters:
    a (float): The numerator.
    b (float): The denominator.
    
    Returns:
    float or None: The result of a / b if b is not zero, otherwise None.
    """
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b
