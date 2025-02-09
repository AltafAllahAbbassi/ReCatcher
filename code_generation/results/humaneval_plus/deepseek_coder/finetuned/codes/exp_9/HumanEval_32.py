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
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("Invalid input. Please provide a list of even number of coefficients "
                         "with largest non zero coefficient as the last coefficient.")

    # Find the largest coefficient
    largest_coeff = max(xs)

    # Find the sign of the largest coefficient
    sign = -1 if largest_coeff < 0 else 1

    # Find the index of the largest coefficient
    largest_index = xs.index(largest_coeff)

    # Calculate the initial guess
    guess = sign * math.pow(math.fabs(largest_coeff), 1 / (largest_index + 1))

    # Iterate until the guess is close enough
    while math.fabs(poly(xs, guess)) > 1e-6:
        guess = guess - poly(xs, guess) / poly([coeff if i!= largest_index else coeff - sign * math.pow(math.fabs(largest_coeff), 1 / (largest_index + 1)) for i, coeff in enumerate(xs)], guess)

    return guess