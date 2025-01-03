def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize current sum and min sum
    cur_sum = 0
    min_sum = float('inf')

    # Iterate through the array
    for num in nums:
        # Update current sum
        cur_sum += num

        # Update min sum
        min_sum = min(min_sum, cur_sum)

        # If current sum is greater than 0, reset it to 0
        if cur_sum > 0:
            cur_sum = 0

    return min_sum