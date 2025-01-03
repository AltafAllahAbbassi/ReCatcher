def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    # 1. 先找出n的所有因子
    # 2. 找出因子中最大的质数
    # 3. 返回质数
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    for factor in factors:
        if is_prime(factor):
            return factor