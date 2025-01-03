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

    # 2. Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # 3. Initialize the grid
    grid = [[(i, j) for j in range(cols)] for i in range(rows)]

    # 4. Initialize the queue
    queue = []

    # 5. Initialize the visited set
    visited = set()

    # 6. Initialize the result
    result = []

    # 7. Initialize the start point
    start = (0, 0)

    # 8. Add the start point to the queue
    queue.append(start)

    # 9. Initialize the distance
    distance = 0

    # 10. Initialize the k
    k = k - 1

    # 11. Loop until the queue is empty
    while queue:
        # 12. Get the size of the queue
        size = len(queue)

        # 13. Loop for the size of the queue
        for _ in range(size):
            # 14. Get the current point
            point = queue.pop(0)

            # 15. Get the row and column of the current point
            row, col = point

            # 16. Get the value of the current point
            value = grid[row][col]

            # 17. Check if the current point is visited
            if value in visited:
                continue

            # 18. Add the current point to the visited set
            visited.add(value)

            # 19. Check if the current point is the destination
            if value == k:
                # 20. Add the value to the result
                result.append(value)

                # 21. Break the loop
                break

            # 22. Check if the current point is the last point
            if row == rows - 1 and col == cols - 1:
                # 23. Add the value to the result
                result.append(value)

                # 24. Break the loop
                break

            # 25. Check if the current point is the last row
            if row == rows - 1:
                # 26. Add the value to the result
                result.append(value)

                # 27. Add the next column to the queue
                queue.append((row, col + 1))

                # 28. Break the loop
                break

            # 29. Check if the current point is the last column
            if col == cols - 1:
                # 30. Add the value to the result
                result.append(value)

                # 31. Add the next row to the queue
                queue.append((row + 1, col))

                # 32. Break the loop
                break

            # 33. Add the next row to the queue
            queue.append((row + 1, col))

            # 34. Add the next column to the queue
            queue.append((row, col + 1))

    # 35. Return the result
    return result