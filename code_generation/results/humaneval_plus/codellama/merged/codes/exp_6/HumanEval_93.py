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
    encoded_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        else:
            encoded_message += char
        
        if char.isalpha() and char in 'aeiouAEIOU':
            index = (i + 2) % 26
            encoded_message += message[i + 1 + index].upper()
    
    return encoded_message