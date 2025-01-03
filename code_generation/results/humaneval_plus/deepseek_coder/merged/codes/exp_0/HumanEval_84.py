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
    # convert the number to binary
    binary_num = bin(N)[2:]
    
    # calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in binary_num)
    
    # convert the sum to binary and return it
    return bin(sum_of_digits)[2:]