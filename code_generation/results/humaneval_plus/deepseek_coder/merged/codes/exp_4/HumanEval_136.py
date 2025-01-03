def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    neg_nums = [i for i in lst if i < 0]
    pos_nums = [i for i in lst if i > 0]

    if not neg_nums:
        largest_neg = None
    else:
        largest_neg = max(neg_nums)

    if not pos_nums:
        smallest_pos = None
    else:
        smallest_pos = min(pos_nums)

    return (largest_neg, smallest_pos)