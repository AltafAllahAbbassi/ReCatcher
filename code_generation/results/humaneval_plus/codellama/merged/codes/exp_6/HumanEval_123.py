def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    odd_numbers = []
    collatz_sequence = [n]

    while collatz_sequence[-1]!= 1:
        previous_term = collatz_sequence[-1]
        if previous_term % 2 == 0:
            collatz_sequence.append(previous_term // 2)
        else:
            collatz_sequence.append(3 * previous_term + 1)

    for term in collatz_sequence:
        if term % 2!= 0:
            odd_numbers.append(term)

    return sorted(odd_numbers)