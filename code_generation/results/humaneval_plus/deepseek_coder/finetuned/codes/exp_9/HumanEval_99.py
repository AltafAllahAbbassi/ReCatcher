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
        # Calculate the difference between the number and the next integer
        diff_next = num - int(num)

        # Calculate the difference between the number and the previous integer
        diff_prev = int(num) + 1 - num

        # Check if the number is equidistant between two integers
        if diff_next == diff_prev:
            # Round the number away from zero
            if num % 2 == 0:
                return int(num)
            else:
                return int(num) + 1

        # Check if the number is closer to the next integer
        elif diff_next < diff_prev:
            return int(num)

        # Check if the number is closer to the previous integer
        else:
            return int(num) + 1

    else:
        # Calculate the difference between the number and the next integer
        diff_next = num - int(num)

        # Calculate the difference between the number and the previous integer
        diff_prev = int(num) - 1 - num

        # Check if the number is equidistant between two integers
        if diff