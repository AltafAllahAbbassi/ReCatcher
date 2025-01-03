def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [2, 3]
    elif n == 4:
        return [2, 3, 5]
    elif n == 5:
        return [2, 3, 5, 7]
    elif n == 6:
        return [2, 3, 5, 7, 11]
    elif n == 7:
        return [2, 3, 5, 7, 11, 13]
    elif n == 8:
        return [2, 3, 5, 7, 11, 13, 17]
    elif n == 9:
        return [2, 3, 5, 7, 11, 13, 17, 19]
    elif n == 10:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n == 11:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    elif n == 12:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    elif n == 13:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n == 14:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    elif n == 15:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    elif n == 16:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    elif n == 17:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    elif n == 18:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    elif n == 19:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    elif n == 20:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    elif n == 21:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61