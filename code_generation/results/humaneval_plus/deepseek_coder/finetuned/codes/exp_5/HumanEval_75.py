def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        count = 0
        for i in range(2, a):
            if a % i == 0:
                count += 1
        if count == 1:
            return True
        else:
            return False
    else:
        return "Number is too large"