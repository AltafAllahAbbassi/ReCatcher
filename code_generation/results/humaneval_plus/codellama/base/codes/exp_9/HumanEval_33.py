def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_new = []
    for i in range(0, len(l), 3):
        l_new.append(l[i])
    l_new.sort()
    for i in range(1, len(l), 3):
        l_new.append(l[i])
    for i in range(2, len(l), 3):
        l_new.append(l[i])
    return l_new