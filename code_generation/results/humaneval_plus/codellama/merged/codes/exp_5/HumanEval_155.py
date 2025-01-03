def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even = 0
    count_odd = 0

    while num!= 0:
        digit = num % 10
        if digit % 2 == 0:
            count_even++
        else:
            count_odd++
        num /= 10

    return Pair(count_even, count_odd)