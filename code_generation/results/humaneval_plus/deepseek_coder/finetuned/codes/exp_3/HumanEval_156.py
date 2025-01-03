def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Define the mapping from integers to roman numerals
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000:'m'
    }

    # Initialize an empty string to store the roman numeral
    roman_numeral = ''

    # Iterate through the roman_numerals dictionary in reverse order
    for numeral, symbol in sorted(roman_numerals.items(), reverse=True):
        # Check if the number is greater than or equal to the current numeral
        while number >= numeral:
            # Add the corresponding roman numeral symbol to the result
            roman_numeral += symbol
            # Subtract the numeral from the number
            number -= numeral

    # Return the roman numeral in lowercase
    return roman_numeral.lower()