from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the string into a list of numbers
    number_list = numbers.split()

    # Sort the list of numbers
    number_list.sort()

    # Join the sorted numbers back into a string
    sorted_numbers =''.join(number_list)

    return sorted_numbers