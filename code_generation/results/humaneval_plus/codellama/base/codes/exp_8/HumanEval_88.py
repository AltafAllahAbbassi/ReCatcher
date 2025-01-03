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
            return [array[1], array[0]]
    if len(array) == 3:
        if array[0] + array[2] % 2 == 0:
            return array
        else:
            return [array[2], array[0], array[1]]
    if len(array) == 4:
        if array[0] + array[3] % 2 == 0:
            return array
        else:
            return [array[3], array[0], array[1], array[2]]
    if len(array) == 5:
        if array[0] + array[4] % 2 == 0:
            return array
        else:
            return [array[4], array[0], array[1], array[2], array[3]]
    if len(array) == 6:
        if array[0] + array[5] % 2 == 0:
            return array
        else:
            return [array[5], array[0], array[1], array[2], array[3], array[4]]
    if len(array) == 7:
        if array[0] + array[6] % 2 == 0:
            return array
        else:
            return [array[6], array[0], array[1], array[2], array[3], array[4], array[5]]
    if len(array) == 8:
        if array[0] + array[7] % 2 == 0:
            return array
        else:
            return [array[7], array[0], array[1], array[2], array[3], array[4], array[5], array[6]]
    if len(array) == 9:
        if array[0] + array[8] % 2 == 0:
            return array
        else:
            return [array[8], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7]]
    if len(array) == 10:
        if array[0] + array[9] % 2 == 0:
            return array
        else:
            return [array[9], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8]]
    if len(array) == 11:
        if array[0] + array[10] % 2 == 0:
            return array
        else:
            return [array[10], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9]]
    if len(array) == 12:
        if array[0] + array[11] % 2 == 0:
            return array
        else:
            return [array[11], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10]]
    if len(array) == 13:
        if array[0] + array[12] % 2 == 0:
            return array
        else:
            return [array[12], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11]]
    if len(array) == 14:
        if array[0] + array[13] % 2 == 0:
            return array
        else:
            return [array[13], array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11], array[12]]
    if len(array) == 15:
        if array[0]