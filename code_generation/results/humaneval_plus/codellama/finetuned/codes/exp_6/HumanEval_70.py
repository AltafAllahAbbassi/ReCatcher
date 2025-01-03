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
    if not lst:
        return []

    result = [min(lst)]
    lst = list(filter(lambda x: x!= min(lst), lst))

    if not lst:
        return result

    result.append(max(lst))
    lst = list(filter(lambda x: x!= max(lst), lst))

    if not lst:
        return result

    result.append(min(lst))
    lst = list(filter(lambda x: x!= min(lst), lst))

    return result + lst