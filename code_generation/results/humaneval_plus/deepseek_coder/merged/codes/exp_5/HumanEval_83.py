def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The count of n-digit numbers that start or end with 1 is 2 * 10^(n-2)
    # because for each n-digit number that starts or ends with 1, there are two
    # possibilities: it starts with 1 or it ends with 1.
    return 2 * 10 ** (n - 2)