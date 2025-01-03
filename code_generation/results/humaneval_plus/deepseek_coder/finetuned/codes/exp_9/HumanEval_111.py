def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Create an empty dictionary to store the count of each letter
    letter_count = {}

    # Split the string into a list of lowercase letters
    letters = test.lower().split()

    # Iterate over each letter in the list
    for letter in letters:
        # Check if the letter is already in the dictionary
        if letter in letter_count:
            # If yes, increment the count by 1
            letter_count[letter] += 1
        else:
            # If no, add the letter to the dictionary with count 1
            letter_count[letter] = 1

    # Find the maximum count among all letters
    max_count = max(letter_count.values())

    # Create a new dictionary to store the letters with the maximum count
    max_letters = {}

    # Iterate over each letter in the letter_count dictionary
    for letter, count in letter_count.items():
        # Check if the count matches the maximum count
        if count == max_count:
            # If yes, add the letter to the max_letters dictionary
            max_letters[letter] = count

    # Return the max_letters dictionary
    return max_letters