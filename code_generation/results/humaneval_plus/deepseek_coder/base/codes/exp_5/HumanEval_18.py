def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring:
        return 0
    if len(substring) > len(string):
        return 0
    if len(substring) == len(string):
        return 1 if substring == string else 0
    if len(substring) == 1:
        return string.count(substring)
    return string.count(substring) + how_many_times(string[1:], substring)