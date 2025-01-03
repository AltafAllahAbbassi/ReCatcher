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

    # Initialize a counter to keep track of the number of open parentheses
    open_count = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Ignore spaces in the input string
        if char =='':
            continue

        # If the character is an open brace, increment the counter
        if char == '(':
            open_count += 1

        # Append the character to the current group string
        current_group += char

        # If the character is a close brace, decrement the counter
        if char == ')':
            open_count -= 1

        # If the counter reaches 0, it means the current group is complete
        if open_count == 0:
            separate_groups.append(current_group)
            current_group = ''

    return separate_groups