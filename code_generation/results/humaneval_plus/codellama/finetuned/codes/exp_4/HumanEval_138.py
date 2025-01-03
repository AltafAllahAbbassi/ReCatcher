def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2!= 0 or n < 6:
        return False

    numbers = [2, 4, 6, 8]
    while len(numbers) < 4:
        numbers.extend([numbers[-1] + 2] * (4 - len(numbers)))

    return n == sum(numbers)