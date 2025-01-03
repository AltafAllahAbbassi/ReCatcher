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
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded += char.lower()
            else:
                encoded += char.upper()
        else:
            encoded += char
    for vowel in vowels:
        encoded = encoded.replace(vowel, chr(ord(vowel) + 2))
    return encoded