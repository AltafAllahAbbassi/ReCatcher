FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # TODO: Implement this function
    # return the number of vowels in the string
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count