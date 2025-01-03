def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Convert the value to a float
    num = float(value)

    # Check if the number is positive or negative
    if num >= 0:
        # Round the number up and convert it to an integer
        rounded_up = int(num + 0.5)
        # Return the rounded up integer
        return rounded_up
    else:
        # Round the number down and convert it to an integer
        rounded_down = int(num - 0.5)
        # Return the rounded down integer
        return rounded_down