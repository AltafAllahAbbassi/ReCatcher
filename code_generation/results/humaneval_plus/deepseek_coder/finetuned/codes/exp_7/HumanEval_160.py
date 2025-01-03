def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Check if the length of operator list is equal to the length of operand list minus one
    if len(operator)!= len(operand) - 1:
        return "Invalid input: Length of operator list should be equal to the length of operand list minus one."

    # Check if all elements in operand list are non-negative integers
    if not all(isinstance(num, int) and num >= 0 for num in operand):
        return "Invalid input: All elements in operand list should be non-negative integers."

    # Check if operator list has at least one operator
    if len(operator) == 0:
        return "Invalid input: Operator list should have at least one operator."

    # Check if operand list has at least two operands
    if len(operand) < 2:
        return "Invalid input: Operand list should have at least two operands."

    # Initialize the result variable with the first element of operand list
    result = operand[0]

    # Iterate over the range of length of operator list
    for i in range(len(operator)):
        # Check if the operator is valid
        if operator[i] not in ['+', '-', '*', '//', '**']:
            return "Invalid input: Operator list should only contain '+', '-', '*', '//', or '**'."

        # Perform the corresponding operation based on the operator
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]

    return result