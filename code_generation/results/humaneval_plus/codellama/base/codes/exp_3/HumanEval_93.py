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
    message = message.lower()
    message = message.replace('a', 'b')
    message = message.replace('e', 'f')
    message = message.replace('i', 'g')
    message = message.replace('o', 'h')
    message = message.replace('u', 'i')
    message = message.replace('b', 'a')
    message = message.replace('f', 'e')
    message = message.replace('g', 'i')
    message = message.replace('h', 'o')
    message = message.replace('i', 'u')
    return message