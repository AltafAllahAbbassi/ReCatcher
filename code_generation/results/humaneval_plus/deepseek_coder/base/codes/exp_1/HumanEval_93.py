def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char.isupper():
            new_message += char.lower()
        elif char.islower():
            new_message += char.upper()
        elif char in vowels:
            new_message += vowels[(vowels.index(char) + 2) % 5]
        else:
            new_message += char
    return new_message