def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def factorial(i):
        if i == 0:
            return 1
        else:
            return i * factorial(i - 1)

    def sum_to_i(i):
        return i * (i + 1) // 2

    return [factorial(i) if i % 2 == 0 else sum_to_i(i) for i in range(1, n + 1)]