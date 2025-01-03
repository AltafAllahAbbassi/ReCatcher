def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return string

    # Find the longest palindrome postfix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            palindrome_suffix = string[-i:]
            break

    # Find the string prefix before the palindrome suffix
    prefix = string[:-len(palindrome_suffix)]

    # Append reverse of prefix to the end of the string
    return string + prefix[::-1]