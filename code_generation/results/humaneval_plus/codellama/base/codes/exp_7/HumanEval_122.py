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
    # Edge cases
    if len(arr) == 0:
        return 0
    if k == 0:
        return 0
    if k == 1:
        return arr[0]

    # Initialize
    sum = 0
    # Iterate over the array
    for i in range(k):
        # If the number is less than 10, add it to the sum
        if arr[i] < 10:
            sum += arr[i]
        # If the number is greater than 10, add the first digit to the sum
        else:
            sum += arr[i] // 10
    return sum