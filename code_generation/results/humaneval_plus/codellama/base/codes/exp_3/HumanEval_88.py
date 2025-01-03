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
        if array[0] + array[1] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 3:
        if array[0] + array[2] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 4:
        if array[0] + array[3] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 5:
        if array[0] + array[4] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 6:
        if array[0] + array[5] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 7:
        if array[0] + array[6] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 8:
        if array[0] + array[7] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 9:
        if array[0] + array[8] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 10:
        if array[0] + array[9] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 11:
        if array[0] + array[10] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 12:
        if array[0] + array[11] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 13:
        if array[0] + array[12] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 14:
        if array[0] + array[13] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 15:
        if array[0] + array[14] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 16:
        if array[0] + array[15] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 17:
        if array[0] + array[16] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 18:
        if array[0] + array[17] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 19:
        if array[0] + array[18] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 20:
        if array[0] + array[19] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 21:
        if array[0] + array[20] % 2 == 0:
            return array
        else:
            return array[::-1]
    if len(array) == 22:
        if array[0] + array[21] % 2 == 0:
            return array