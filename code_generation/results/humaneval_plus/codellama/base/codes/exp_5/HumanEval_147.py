def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # 1 <= n <= 1000
    # 1 <= a[i] <= 1000
    # 1 <= i < j < k <= n
    # a[i] + a[j] + a[k] is a multiple of 3

    # Solution:
    # 1. Create a list of all the numbers from 1 to n.
    # 2. Iterate through the list and check if the sum of any two numbers is a multiple of 3.
    # 3. If the sum is a multiple of 3, increment the count.
    # 4. Return the count.

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    # Code:
    # Create a list of all the numbers from 1 to n.
    a = list(range(1, n+1))

    # Iterate through the list and check if the sum of any two numbers is a multiple of 3.
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 3 == 0:
                count += 1

    # Return the count.
    return count