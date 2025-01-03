def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = float('inf')

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subArray = nums[i:j]
            if len(subArray) > 0:
                currentSum = sum(subArray)
                if currentSum < minSum:
                    minSum = currentSum

    return minSum