from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    results = []

    for group in groups:
        count = 0
        max_count = 0

        for char in group:
            if char == '(':
                count++
                if count > max_count:
                    max_count = count
            elif char == ')':
                count--

        results.append(max_count)

    return results