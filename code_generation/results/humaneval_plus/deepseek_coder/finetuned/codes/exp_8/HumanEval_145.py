def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Create a dictionary to store the sum of digits for each number
    digits_sum = {}
    for num in nums:
        digits_sum[num] = sum(int(digit) for digit in str(abs(num)))

    # Sort the numbers based on their sum of digits
    sorted_nums = sorted(nums, key=lambda x: (digits_sum[x], nums.index(x)))

    return sorted_nums