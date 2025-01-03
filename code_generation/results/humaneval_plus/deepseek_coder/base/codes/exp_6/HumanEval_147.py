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
    # 1. Create an array of length n
    # 2. For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    # 3. Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    # and a[i] + a[j] + a[k] is a multiple of 3.
    # 4. Create a counter for the number of triples
    # 5. Loop through the array
    # 6. If the sum of the triple is a multiple of 3, increment the counter
    # 7. Return the counter
    # 8. Time complexity: O(n)
    # 9. Space complexity: O(n)
    # 10. Create an array of length n
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # 11. Create a counter for the number of triples
    count = 0
    # 12. Loop through the array
    for i in range(n):
        # 13. Loop through the array
        for j in range(i + 1, n):
            # 14. Loop through the array
            for k in range(j + 1, n):
                # 15. If the sum of the triple is a multiple of 3, increment the counter
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    # 16. Return the counter
    return count