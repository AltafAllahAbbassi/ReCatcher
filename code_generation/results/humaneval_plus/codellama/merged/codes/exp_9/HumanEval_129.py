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
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    minPath = [None] * k
    minPathLen = k

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                queue = [(i, j)]
                step = 1

                while queue:
                    current = queue.pop(0)
                    x, y = current[0], current[1]

                    if step == k:
                        for i in range(k):
                            minPath[i] = grid[x][y]
                    else:
                        if x > 0 and not visited[x - 1][y]:
                            visited[x - 1][y] = True
                            queue.append((x - 1, y))
                        if x < N - 1 and not visited[x + 1][y]:
                            visited[x + 1][y] = True
                            queue.append((x + 1, y))
                        if y > 0 and not visited[x][y - 1]:
                            visited[x][y - 1] = True
                            queue.append((x, y - 1))
                        if y < N - 1 and not visited[x][y + 1]:
                            visited[x][y + 1] = True
                            queue.append((x, y + 1))

                    step++

                if step == minPathLen:
                    for i in range(k):
                        if minPath[i]!= None:
                            minPath[i] = grid[x][y]

    return minPath