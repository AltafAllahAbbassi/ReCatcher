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
    N = len(grid)

    # 3. Initialize the distance matrix
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]

    # 4. Initialize the distance matrix
    distance[0][0] = grid[0][0]

    # 5. Initialize the queue
    queue = [(0, 0)]

    # 6. BFS
    while queue:
        # 6.1. Get the current cell
        x, y = queue.pop(0)

        # 6.2. Get the current distance
        d = distance[x][y]

        # 6.3. Get the neighbors
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        # 6.4. Iterate over the neighbors
        for i, j in neighbors:
            # 6.4.1. Check if the neighbor is valid
            if 0 <= i < N and 0 <= j < N:
                # 6.4.2. Check if the neighbor is not visited
                if distance[i][j] == float('inf'):
                    # 6.4.3. Update the distance
                    distance[i][j] = d + grid[i][j]
                    # 6.4.4. Add the neighbor to the queue
                    queue.append((i, j))

    # 7. Initialize the path
    path = []

    # 8. Iterate over the distance matrix
    for i in range(N):
        for j in range(N):
            # 8.1. Check if the cell is the starting cell
            if distance[i][j] == k:
                # 8.2. Add the cell to the path
                path.append(grid[i][j])

    # 9. Return the path
    return path