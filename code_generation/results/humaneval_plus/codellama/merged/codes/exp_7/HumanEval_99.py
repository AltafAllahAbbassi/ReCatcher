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
    try:
        value = float(value)
    except ValueError:
        return "Invalid input. Please provide a valid number."

    if value == int(value):
        return int(value)

    integers = list(range(int(value) - 10, int(value) + 10))
    closest = min(integers, key=lambda x: abs(x - value))

    if abs(closest) < abs(0.5 * (closest - value)):
        return closest
    else:
        return closest if closest * value > 0 else closest - 1