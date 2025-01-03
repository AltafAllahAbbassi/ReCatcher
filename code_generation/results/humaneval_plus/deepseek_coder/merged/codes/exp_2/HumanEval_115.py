import math

def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Initialize the count of buckets to 0
    count = 0
    # Flatten the grid into a list of wells
    wells = [well for row in grid for well in row]
    # Sort the wells in ascending order
    wells.sort()
    # Initialize the left and right pointers
    left, right = 0, len(wells) - 1
    # While the left pointer is less than the right pointer
    while left < right:
        # If the well at the left pointer is less than the well at the right pointer
        if wells[left] < wells[right]:
            # Increment the count by the difference between the well at the right pointer and the well at the left pointer
            count += wells[right] - wells[left]
            # Increment the left pointer
            left += 1
        else:
            # Otherwise, decrement the right pointer
            right -= 1
    # Return the count
    return count