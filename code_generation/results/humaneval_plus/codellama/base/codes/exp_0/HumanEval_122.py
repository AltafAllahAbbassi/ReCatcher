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
    # Edge case
    if k == 0:
        return 0

    # Sort the array
    arr.sort()

    # Initialize the sum
    sum = 0

    # Iterate over the first k elements
    for i in range(k):
        # If the element is less than 100, add it to the sum
        if arr[i] < 100:
            sum += arr[i]

    return sum