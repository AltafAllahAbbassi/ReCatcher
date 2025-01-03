def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    if N <= 0 or N > 10000:
        return "Invalid input. Please provide a positive integer between 0 and 10000."
    
    binary = bin(N)[2:]
    total_sum = 0
    
    for digit in binary:
        total_sum += int(digit)
    
    return str(total_sum)