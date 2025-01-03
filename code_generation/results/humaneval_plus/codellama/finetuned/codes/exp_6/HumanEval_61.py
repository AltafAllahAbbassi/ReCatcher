def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    open_brackets = 0
    for char in brackets:
        if char == "(":
            open_brackets++
        elif char == ")":
            if open_brackets == 0:
                return False
            open_brackets--
    return open_brackets == 0