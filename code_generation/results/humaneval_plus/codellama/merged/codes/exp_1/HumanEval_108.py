def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        if num < 0:
            sign_digit = -1 * (num % 10)
            if sign_digit > 0:
                count++
        else:
            sum_of_digits = 0
            for digit in num.toString().digits():
                sum_of_digits += digit
            if sum_of_digits > 0:
                count++
    return count