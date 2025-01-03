def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    count = 0
    two_digits = 0
    sum_elements = 0

    while count < k:
        if len(str(arr[count])) <= 2:
            two_digits++
        sum_elements += arr[count]
        count++

    return sum_elements