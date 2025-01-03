def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Write your code here
    if not nums:
        return 0
    min_sum = float('inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum < min_sum:
            min_sum = cur_sum
        if cur_sum > 0:
            cur_sum = 0
    return min_sum