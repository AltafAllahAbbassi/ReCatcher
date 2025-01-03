def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []
    if len(array) == 1:
        return array
    if len(array) == 2:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 3:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 4:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 5:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 6:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 7:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 8:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 9:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 10:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 11:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 12:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 13:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 14:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 15:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 16:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 17:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 18:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 19:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 20:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 21:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 22:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 23:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 24:
        if sum(array) % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 25:
        if sum(array)