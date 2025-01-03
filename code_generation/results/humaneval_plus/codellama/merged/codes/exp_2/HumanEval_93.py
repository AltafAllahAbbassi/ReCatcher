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
    encoded = ''
    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        else:
            encoded += char
        
        if char.isalpha() and char in 'aeiouAEIOU':
            encoded += message[(i + 2) % len(message)]
        
    return encoded