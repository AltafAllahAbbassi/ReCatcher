def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    # Convert the hexadecimal number to a string
    num = str(num)

    # Initialize a counter variable
    count = 0

    # Iterate over each character in the string
    for char in num:
        # Check if the character is a hexadecimal digit
        if char.isdigit():
            # Convert the digit to decimal
            decimal_value = int(char, 16)
        else:
            # Convert the letter to decimal
            decimal_value = ord(char) - 55

        # Check if the decimal value is prime
        if decimal_value in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            count += 1

    return count