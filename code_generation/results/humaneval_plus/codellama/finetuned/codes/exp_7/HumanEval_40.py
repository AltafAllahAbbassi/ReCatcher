def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    if len(l) < 3:
        return False

    for i in range(len(l) - 2):
        if l[i] == 0:
            continue
        for j in range(i + 1, len(l) - 1):
            if l[j] == 0:
                continue
            for k in range(j + 1, len(l)):
                if l[k] == 0:
                    continue
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False