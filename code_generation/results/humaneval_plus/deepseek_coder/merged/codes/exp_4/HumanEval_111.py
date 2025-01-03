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
    # Your code here
    # Initialize an empty dictionary
    histogram_dict = {}
    # Split the string into a list of words
    words = test.split()
    # Iterate over the list of words
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in histogram_dict:
            histogram_dict[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            histogram_dict[word] = 1
    # Find the maximum count
    max_count = max(histogram_dict.values())
    # Iterate over the dictionary and keep only the words with the maximum count
    for word in list(histogram_dict.keys()):
        if histogram_dict[word] < max_count:
            del histogram_dict[word]
    # Return the resulting dictionary
    return histogram_dict