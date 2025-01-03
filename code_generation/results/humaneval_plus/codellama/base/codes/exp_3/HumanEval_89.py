def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[2:] + alphabet[:2]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[:26]
    new_alphabet = new_alphabet.replace(' ', '')
    new_alphabet = new_alphabet.replace('\n', '')
    new_alphabet = new_alphabet.replace('\r', '')
    new_alphabet = new_alphabet.replace('\t', '')
    new_alphabet = new_alphabet.replace('\x0b', '')
    new_alphabet = new_alphabet.replace('\x0c', '')
    new_alphabet = new_alphabet.replace('\x0d', '')
    new_alphabet = new_alphabet.replace('\x0e', '')
    new_alphabet = new_alphabet.replace('\x0f', '')
    new_alphabet = new_alphabet.replace('\x10', '')
    new_alphabet = new_alphabet.replace('\x11', '')
    new_alphabet = new_alphabet.replace('\x12', '')
    new_alphabet = new_alphabet.replace('\x13', '')
    new_alphabet = new_alphabet.replace('\x14', '')
    new_alphabet = new_alphabet.replace('\x15', '')
    new_alphabet = new_alphabet.replace('\x16', '')
    new_alphabet = new_alphabet.replace('\x17', '')
    new_alphabet = new_alphabet.replace('\x18', '')
    new_alphabet = new_alphabet.replace('\x19', '')
    new_alphabet = new_alphabet.replace('\x1a', '')
    new_alphabet = new_alphabet.replace('\x1b', '')
    new_alphabet = new_alphabet.replace('\x1c', '')
    new_alphabet = new_alphabet.replace('\x1d', '')
    new_alphabet = new_alphabet.replace('\x1e', '')
    new_alphabet = new_alphabet.replace('\x1f', '')
    new_alphabet = new_alphabet.replace('\x20', '')
    new_alphabet = new_alphabet.replace('\x21', '')
    new_alphabet = new_alphabet.replace('\x22', '')
    new_alphabet = new_alphabet.replace('\x23', '')
    new_alphabet = new_alphabet.replace('\x24', '')
    new_alphabet = new_alphabet.replace('\x25', '')
    new_alphabet = new_alphabet.replace('\x26', '')
    new_alphabet = new_alphabet.replace('\x27', '')
    new_alphabet = new_alphabet.replace('\x28', '')
    new_alphabet = new_alphabet.replace('\x29', '')
    new_alphabet = new_alphabet.replace('\x2a', '')
    new_alphabet = new_alphabet.replace('\x2b', '')
    new_alphabet = new_alphabet.replace('\x2c', '')
    new_alphabet = new_alphabet.replace('\x2d', '')
    new_alphabet = new_alphabet.replace('\x2e', '')
    new_alphabet = new_alphabet.replace('\x2f', '')
    new_alphabet = new_alphabet.replace('\x30', '')
    new_alphabet = new_alphabet.replace('\x31', '')
    new_alphabet = new_alphabet.replace('\x32', '')
    new_alphabet = new_alphabet.replace('\x33', '')
    new_alphabet = new_alphabet.replace('\x34', '')
    new_alphabet = new_alphabet.replace('\x35', '')
    new_alphabet = new_alphabet.replace('\x36', '')
    new_alphabet = new_alphabet.replace('\x37', '')
    new_alphabet = new_alphabet.replace('\x38', '')
    new_alphabet = new_alphabet.replace('\x39', '')