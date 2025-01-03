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
    fib_numbers = [0, 1]
    prime_numbers = []
    i = 2
    while len(prime_numbers) < n:
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
        if is_prime(fib_numbers[i]):
            prime_numbers.append(fib_numbers[i])
        i += 1
    return prime_numbers[-1]