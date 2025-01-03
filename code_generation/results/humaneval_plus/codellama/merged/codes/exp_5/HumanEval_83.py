def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for num in range(10 ** n):
        if str(num)[0] == '1' or str(num)[-1] == '1':
            count++
    return count