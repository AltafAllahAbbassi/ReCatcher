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
    new_alphabet = new_alphabet[2:] + new_alphabet[:2]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[4:] + new_alphabet[:4]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[8:] + new_alphabet[:8]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[16:] + new_alphabet[:16]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[32:] + new_alphabet[:32]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[64:] + new_alphabet[:64]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[128:] + new_alphabet[:128]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[256:] + new_alphabet[:256]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[512:] + new_alphabet[:512]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[1024:] + new_alphabet[:1024]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[2048:] + new_alphabet[:2048]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[4096:] + new_alphabet[:4096]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[8192:] + new_alphabet[:8192]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[16384:] + new_alphabet[:16384]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[32768:] + new_alphabet[:32768]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[65536:] + new_alphabet[:65536]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[131072:] + new_alphabet[:131072]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[262144:] + new_alphabet[:262144]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[524288:] + new_alphabet[:524288]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[1048576:] + new_alphabet[:1048576]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[2097152:] + new_alphabet[:2097152]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[4194304:] + new_alphabet[:4194304]
    new_alphabet = new_alphabet * 2
    new_alphabet = new_alphabet[8388608:] + new_alphabet[:8388608]
    new_alphabet = new_alphabet * 2
    new_