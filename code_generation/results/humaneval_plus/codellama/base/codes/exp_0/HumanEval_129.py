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

    # 2. Get the dimensions of the grid
    n = len(grid)
    m = len(grid[0])

    # 3. Initialize the grid
    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = (i + 1) * m + j + 1

    # 4. Initialize the queue
    queue = [(0, 0, 0)]

    # 5. Initialize the visited set
    visited = set()

    # 6. Initialize the answer
    answer = []

    # 7. Loop until the queue is empty
    while queue:
        # 8. Get the current node
        node = queue.pop(0)

        # 9. Get the current row, column and path length
        row, col, path_len = node[0], node[1], node[2]

        # 10. Check if the current node is visited
        if (row, col) in visited:
            continue

        # 11. Check if the current node is the goal
        if path_len == k:
            answer = grid[row][col]
            break

        # 12. Add the current node to the visited set
        visited.add((row, col))

        # 13. Add the neighbors to the queue
        for i in range(4):
            new_row = row + row_offsets[i]
            new_col = col + col_offsets[i]
            if 0 <= new_row < n and 0 <= new_col < m:
                queue.append((new_row, new_col, path_len + 1))

    # 14. Return the answer
    return answer