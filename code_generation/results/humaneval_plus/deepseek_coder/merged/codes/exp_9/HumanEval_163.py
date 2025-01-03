def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Initialize an empty list to store the even digits
    even_digits = []

    # Iterate through the range from a to b
    for i in range(a, b + 1):
        # Convert the integer to a string
        str_i = str(i)
        # Iterate through each character in the string
        for char in str_i:
            # Convert the character back to an integer
            int_char = int(char)
            # Check if the integer is even
            if int_char % 2 == 0:
                # If it is, add it to the list
                even_digits.append(int_char)

    # Sort the list in ascending order
    even_digits.sort()

    # Return the list of even digits
    return even_digits