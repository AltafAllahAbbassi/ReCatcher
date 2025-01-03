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

    # 2. Initialize the grid
    N = len(grid)
    grid = [[-1] + row for row in grid]
    grid = [[-1] * N + col for col in grid]

    # 3. Initialize the distance matrix
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = 0

    # 4. Initialize the queue
    queue = [(0, 0)]

    # 5. BFS
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] > distance[x][y] + 1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    # 6. Find the minimum path
    min_path = []
    x, y = N - 1, N - 1
    while x >= 0 and y >= 0:
        min_path.append(grid[x][y])
        x, y = x - dx[grid[x][y]], y - dy[grid[x][y]]
    return min_path[::-1]