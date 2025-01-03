from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    result = []
    temp = ""
    for char in paren_string:
        if char == " ":
            continue
        if char == "(":
            if temp:
                stack.append(temp)
                temp = ""
            stack.append(char)
        if char == ")":
            stack.append(char)
            temp = "".join(stack[-2:])
            if temp.count("(") == temp.count(")"):
                stack = stack[:-2]
                result.append(temp)
                temp = ""
    return result