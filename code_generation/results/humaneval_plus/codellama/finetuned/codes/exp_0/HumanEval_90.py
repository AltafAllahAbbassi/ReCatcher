def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) < 2:
        return None
    
    smallest = lst[0]
    second_smallest = None
    
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest or second_smallest is None:
            second_smallest = lst[i]
    
    return second_smallest