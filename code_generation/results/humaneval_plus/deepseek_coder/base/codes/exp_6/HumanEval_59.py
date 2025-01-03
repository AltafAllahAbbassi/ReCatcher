def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    # 1. 先找出所有因子
    # 2. 找出所有因子中的质数
    # 3. 找出所有质数中的最大值
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    primes = []
    for i in factors:
        if is_prime(i):
            primes.append(i)
    return max(primes)