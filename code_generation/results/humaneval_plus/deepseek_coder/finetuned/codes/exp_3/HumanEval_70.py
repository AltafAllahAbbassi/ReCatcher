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
        return lst

    sorted_lst = sorted(lst)
    strange_lst = []
    for i in range(len(sorted_lst) // 2):
        strange_lst.append(sorted_lst[i])
        strange_lst.append(sortedorted_lst[-(i + 1)])

    if len(sorted_lst) % 2!= 0:
        strange_lst.append(sorted_lst[len(sorted_lst) // 2])

    return strange_lst