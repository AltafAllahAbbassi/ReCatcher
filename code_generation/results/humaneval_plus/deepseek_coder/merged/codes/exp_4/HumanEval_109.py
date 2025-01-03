def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    # Your code goes here
    # Check if the array is empty
    if not arr:
        return True

    # Find the index of the first element that is greater than its next element
    index = 0
    while index < len(arr) - 1 and arr[index] <= arr[index + 1]:
        index += 1

    # Check if the remaining elements are greater than the first element
    while index < len(arr) - 1 and arr[index] <= arr[index + 1]:
        index += 1
    else:
        if index == len(arr) - 1 and arr[index] <= arr[0]:
            return True

    # Check if the remaining elements are greater than the first element after
    # performing a right shift operation
    index = 0
    while index < len(arr) - 1 and arr[index] <= arr[index + 1]:
        index += 1
    else:
        if index == len(arr) - 1 and arr[index] <= arr[0]:
            return True

    return False