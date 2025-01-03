def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    if n == 0:
        return 0
    else:
        return reduce(lambda x, y: x*y, [i for i in str(n) if i%2 == 1])