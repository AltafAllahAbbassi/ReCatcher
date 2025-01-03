def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    min_path = []

    # Generate all possible paths of length k
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            for _ in range(k - 1):
                # Find the neighbor cells with the smallest value
                min_val = float('inf')
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if x == i and y == j:
                            continue
                        if grid[x][y] < min_val:
                            min_val = grid[x][y]
                            min_i, min_j = x, y

                # Append the value of the neighbor cell to the path
                path.append(grid[min_i][min_j])
                i, j = min_i, min_j

            # Check if the current path is smaller than the minimum path found so far
            if not min_path or path < min_path:
                min_path = path

    return min_path