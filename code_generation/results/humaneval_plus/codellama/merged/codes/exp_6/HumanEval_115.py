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
    rows, cols = grid.shape
    bucket_capacity = capacity

    # Initialize the number of times we need to lower the buckets
    num_times = 0

    # Iterate over each row in the grid
    for i in range(rows):
        # Iterate over each column in the grid
        for j in range(cols):
            # Check if the current cell has water
            if grid[i, j] == 1:
                # Calculate the number of units of water in the well
                num_units = grid[i, :].sum()

                # Check if the bucket has enough capacity to empty the well
                if num_units <= bucket_capacity:
                    # Lower the bucket to empty the well
                    grid[i, :] = 0
                else:
                    # Calculate the number of times we need to lower the bucket
                    num_times += math.ceil(num_units / bucket_capacity)

                    # Lower the bucket to empty the well
                    grid[i, :] = 0
    return num_times