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
    # TODO: Implement max_fill
    # return the number of times you need to lower the buckets
    # to empty the wells
    # grid -> 2D list of integers
    # capacity -> integer
    # return -> integer

    # initialize the number of times you need to lower the buckets
    # to empty the wells
    # to 0
    num_times = 0

    # get the length of the wells
    # well_length -> integer
    well_length = len(grid[0])

    # get the number of wells
    # num_wells -> integer
    num_wells = len(grid)

    # get the number of buckets
    # num_buckets -> integer
    num_buckets = capacity

    # get the number of wells that are full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are completely empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially empty
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are completely empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially empty
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are completely empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially empty
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are completely empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially empty
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    # num_full_wells -> integer
    num_full_wells = 0

    # get the number of wells that are completely empty
    # num_empty_wells -> integer
    num_empty_wells = 0

    # get the number of wells that are partially empty
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are partially full
    # num_partial_wells -> integer
    num_partial_wells = 0

    # get the number of wells that are completely full
    #