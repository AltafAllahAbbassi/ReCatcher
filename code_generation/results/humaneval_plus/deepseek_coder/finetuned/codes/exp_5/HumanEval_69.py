def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Create a dictionary to store the frequency of each integer
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    # Find the greatest integer that satisfies the condition
    greatest = -1
    for num in freq:
        if num > 0 and freq[num] >= num:
            greatest = max(greatest, num)

    return greatest