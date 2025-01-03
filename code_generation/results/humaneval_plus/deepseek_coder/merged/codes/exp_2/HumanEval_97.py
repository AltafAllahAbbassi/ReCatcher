def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # get the unit digits
    a_unit_digit = abs(a) % 10
    b_unit_digit = abs(b) % 10
    # return the product of the unit digits
    return a_unit_digit * b_unit_digit