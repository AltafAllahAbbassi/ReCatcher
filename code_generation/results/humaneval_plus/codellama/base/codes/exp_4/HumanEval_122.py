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
    if len(arr) == 0:
        return 0
    # Base case
    if k == 0:
        return 0
    # Recursive case
    if k == 1:
        return arr[0]
    # Recursive case
    if k == 2:
        return arr[0] + arr[1]
    # Recursive case
    if k == 3:
        return arr[0] + arr[1] + arr[2]
    # Recursive case
    if k == 4:
        return arr[0] + arr[1] + arr[2] + arr[3]
    # Recursive case
    if k == 5:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
    # Recursive case
    if k == 6:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5]
    # Recursive case
    if k == 7:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6]
    # Recursive case
    if k == 8:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7]
    # Recursive case
    if k == 9:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8]
    # Recursive case
    if k == 10:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9]
    # Recursive case
    if k == 11:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10]
    # Recursive case
    if k == 12:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10] + arr[11]
    # Recursive case
    if k == 13:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10] + arr[11] + arr[12]
    # Recursive case
    if k == 14:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10] + arr[11] + arr[12] + arr[13]
    # Recursive case
    if k == 15:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10] + arr[11] + arr[12] + arr[13] + arr[14]
    # Recursive case
    if k == 16:
        return arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9] + arr[10] + arr[11] + arr[12] + arr[13] + arr[14] + arr[15]
    # Recursive case
    if k == 17:
        return arr[0]