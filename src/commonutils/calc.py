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

def simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate the simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): Annual interest rate as a percentage.
    time (float): Time in years.

    Returns:
    float: The simple interest earned.
    """
    return round((principal * rate * time) / 100, 2)


def compound_interest(principal: float, rate: float, time: float, compounds_per_year: int = 1) -> float:
    """
    Calculate the compound interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): Annual interest rate as a percentage.
    time (float): Time in years.
    compounds_per_year (int): Number of times interest is compounded per year.

    Returns:
    float: The compound interest earned.
    """
    amount = principal * (1 + (rate / 100) / compounds_per_year) ** (compounds_per_year * time)
    return round(amount - principal, 2)
