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
    if not (1 <= number <= 1000):
        raise ValueError("Invalid input. Please provide a number between 1 and 1000.")

    roman_num = ""
    while number > 0:
        if number >= 1000:
            roman_num += "m"
            number -= 1000
        elif number >= 500:
            roman_num += "d"
            number -= 500
        elif number >= 100:
            roman_num += "c"
            number -= 100
        elif number >= 50:
            roman_num += "l"
            number -= 50
        elif number >= 10:
            roman_num += "x"
            number -= 10
        else:
            roman_num += "v"
            number -= 5

    return roman_num.lower()