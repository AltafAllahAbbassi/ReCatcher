from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to store the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of open and close braces
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Ignore spaces in the input string
        if char =='':
            continue

        # Add the character to the current group
        current_group += char

        # Increment the balance based on the character
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        # If the balance becomes 0, it means the current group is complete
        if balance == 0:
            separate_groups.append(current_group)
            current_group = ''

    return separate_groups