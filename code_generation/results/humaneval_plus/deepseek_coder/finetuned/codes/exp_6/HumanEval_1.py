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
    current_group = ""

    # Initialize a counter to keep track of the number of open parentheses
    open_count = 0

    # Iterate through each character in the input string
    for char in paren_string:
        # Ignore spaces in the input string
        if char == " ":
            continue

        # If the character is an open brace, increment the counter and add it to the current group
        elif char == "(":
            open_count += 1
            current_group += char

        # If the character is a close brace, decrement the counter and add it to the current group
        elif char == ")":
            open_count -= 1
            current_group += char

        # If the counter becomes negative, it means there are more close braces than open braces,
        # so we need to reset the current group and continue to the next character
        if open_count < 0:
            current_group = ""
            open_count = 0
            continue

        # If the counter is zero, it means we have found a balanced group, so we add it to the separate groups list
        if open_count == 0:
            separate_groups.append(current_group)
            current_group = ""

    return separate_groups