def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        return [min(lst), max(lst)]
    if len(lst) == 3:
        return [min(lst), max(lst), min(lst)]
    if len(lst) == 4:
        return [min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 5:
        return [min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 6:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 7:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 8:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 9:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 10:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 11:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 12:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 13:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 14:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 15:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst)]
    if len(lst) == 16:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst)]
    if len(lst) == 17:
        return [min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min(lst), max(lst), min