import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 == 1:
        raise ValueError("Number of coefficients must be even.")
    if xs[-1] == 0:
        raise ValueError("Largest coefficient cannot be zero.")

    # Find the largest coefficient
    largest_coeff = max(xs)

    # Initialize the search interval
    lower_bound = -largest_coeff
    upper_bound = largest_coeff

    # Perform bisection search
    while True:
        mid_point = (lower_bound + upper_bound) / 2
        if abs(poly(xs, mid_point)) < 1e-6:
            return mid_point
        elif poly(xs, mid_point) > 0:
            lower_bound = mid_point
        else:
            upper_bound = mid_point