def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    x_num, x_den, n_num, n_den = int(x_num), int(x_den), int(n_num), int(n_den)
    if x_den % n_den == 0:
        x_num *= n_den // x_den
        x_den = n_den
    elif n_den % x_den == 0:
        n_num *= x_den // n_den
        n_den = x_den
    else:
        x_num *= n_den
        n_num *= x_den
        x_den *= n_den
    return x_num == n_num