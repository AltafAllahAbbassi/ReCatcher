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
    elif len(lst) == 1:
        return lst
    else:
        lst.sort()
        new_lst = []
        for i in range(len(lst)//2):
            new_lst.append(lst[i])
            new_lst.append(lst[-(i+1)])
        if len(lst) % 2!= 0:
            new_lst.append(lst[len(lst)//2])
        return new_lst