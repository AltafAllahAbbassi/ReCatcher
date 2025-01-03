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
    # 1. Check if the grid is valid
    if not grid or not grid[0]:
        return []

    # 2. Get the size of the grid
    n = len(grid)

    # 3. Initialize the grid
    grid = [[-1] * n for _ in range(n)]

    # 4. Initialize the queue
    queue = [(0, 0, 0, [])]

    # 5. Loop until the queue is empty
    while queue:
        # 6. Get the current cell
        x, y, k, path = queue.pop(0)

        # 7. Check if the cell is valid
        if x < 0 or x >= n or y < 0 or y >= n or grid[x][y]!= -1:
            continue

        # 8. Add the cell to the path
        path.append(grid[x][y])

        # 9. Check if the path is valid
        if k == 0:
            return path

        # 10. Add the cell to the grid
        grid[x][y] = 1

        # 11. Add the neighbors to the queue
        queue.append((x + 1, y, k - 1, path))
        queue.append((x - 1, y, k - 1, path))
        queue.append((x, y + 1, k - 1, path))
        queue.append((x, y - 1, k - 1, path))

    # 12. Return the path
    return []