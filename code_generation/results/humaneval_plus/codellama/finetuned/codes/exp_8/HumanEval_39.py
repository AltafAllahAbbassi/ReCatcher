def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

    for i in range(n):
        fib_number = fib_numbers[i]
        if fib_number in primes:
            return fib_number

        for j in range(len(primes)):
            if primes[j] > fib_number:
                break

            if fib_number % primes[j] == 0:
                break
        else:
            primes.append(fib_number)

    return primes[n]