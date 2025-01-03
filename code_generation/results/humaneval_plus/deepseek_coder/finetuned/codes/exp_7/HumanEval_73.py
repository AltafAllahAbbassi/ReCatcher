def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Check if the array is already palindromic
    if arr == arr[::-1]:
        return 0

    # Initialize the count of changes
    count = 0

    # Iterate through the array
    for i in range(len(arr) // 2):
        # Check if the elements at the beginning and end are different
        if arr[i]!= arr[-(i + 1)]:
            # Increment the count of changes
            count += 1

    return count