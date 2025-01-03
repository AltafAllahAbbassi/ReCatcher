def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_digits = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_digits *= digit
        n //= 10
    return odd_digits