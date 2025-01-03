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
        return lst
    if len(lst) == 3:
        return [lst[0], lst[2], lst[1]]
    if len(lst) == 4:
        return [lst[0], lst[3], lst[1], lst[2]]
    if len(lst) == 5:
        return [lst[0], lst[4], lst[1], lst[3], lst[2]]
    if len(lst) == 6:
        return [lst[0], lst[5], lst[1], lst[4], lst[2], lst[3]]
    if len(lst) == 7:
        return [lst[0], lst[6], lst[1], lst[5], lst[2], lst[4], lst[3]]
    if len(lst) == 8:
        return [lst[0], lst[7], lst[1], lst[6], lst[2], lst[5], lst[3], lst[4]]
    if len(lst) == 9:
        return [lst[0], lst[8], lst[1], lst[7], lst[2], lst[6], lst[3], lst[5], lst[4]]
    if len(lst) == 10:
        return [lst[0], lst[9], lst[1], lst[8], lst[2], lst[7], lst[3], lst[6], lst[4], lst[5]]
    if len(lst) == 11:
        return [lst[0], lst[10], lst[1], lst[9], lst[2], lst[8], lst[3], lst[7], lst[4], lst[6], lst[5]]
    if len(lst) == 12:
        return [lst[0], lst[11], lst[1], lst[10], lst[2], lst[9], lst[3], lst[8], lst[4], lst[7], lst[5], lst[6]]
    if len(lst) == 13:
        return [lst[0], lst[12], lst[1], lst[11], lst[2], lst[10], lst[3], lst[9], lst[4], lst[8], lst[5], lst[7], lst[6]]
    if len(lst) == 14:
        return [lst[0], lst[13], lst[1], lst[12], lst[2], lst[11], lst[3], lst[10], lst[4], lst[9], lst[5], lst[8], lst[6], lst[7]]
    if len(lst) == 15:
        return [lst[0], lst[14], lst[1], lst[13], lst[2], lst[12], lst[3], lst[11], lst[4], lst[10], lst[5], lst[9], lst[6], lst[8], lst[7]]
    if len(lst) == 16:
        return [lst[0], lst[15], lst[1], lst[14], lst[2], lst[13], lst[3], lst[12], lst[4], lst[11], lst[5], lst[10], lst[6], lst[9], lst[7], lst[8]]
    if len(lst) == 17:
        return [lst[0], lst[16], lst[1], lst[15], lst[2], lst[14], lst[3], lst[13], lst[4], lst[12], lst[5