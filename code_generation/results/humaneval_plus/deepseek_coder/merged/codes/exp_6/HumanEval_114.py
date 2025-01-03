def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum subarray sum to be the maximum possible value
    min_sum = float('inf')
    # Initialize the current sum to be 0
    curr_sum = 0
    # Iterate through the array
    for num in nums:
        # Update the current sum
        curr_sum += num
        # Update the minimum sum if the current sum is smaller
        min_sum = min(min_sum, curr_sum)
        # If the current sum is greater than 0, reset it to 0
        if curr_sum > 0:
            curr_sum = 0
    return min_sum