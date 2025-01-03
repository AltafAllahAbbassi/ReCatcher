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

    # Iterate through each character in the input string
    for char in paren_string:
        # Ignore spaces in the input string
        if char =='':
            continue

        # If the character is an open brace, increment the counter
        elif char == '(':
            open_count += 1

        # If the character is a close brace
        elif char == ')':
            # Decrement the counter
            open_count -= 1

            # If the counter becomes negative, it means there are more close braces than open braces
            # Reset the current group and continue to the next character
            if open_count < 0:
                current_group = ''
                open_count = 0
                continue

            # If the counter is zero, it means the current group is complete
            # Append the group to the list of separate groups and reset the current group
            elif open_count == 0:
                separate_groups.append(current_group)
                current_group = ''

        # If the character is not a brace, append it to the current group
        else:
            current_group += char

    # Return the list of separate groups
    return separate_groups