def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 10
    else:
        return 9 * starts_one_ends(n - 1)