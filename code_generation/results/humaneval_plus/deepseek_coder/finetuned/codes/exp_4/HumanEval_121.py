def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Initialize the sum variable
    total_sum = 0

    # Iterate over the list using a for loop
    for i in range(len(lst)):
        # Check if the current element is in an even position and is odd
        if i % 2 == 0 and lst[i] % 2!= 0:
            # Add the element to the sum
            total_sum += lst[i]

    # Return the final sum
    return total_sum