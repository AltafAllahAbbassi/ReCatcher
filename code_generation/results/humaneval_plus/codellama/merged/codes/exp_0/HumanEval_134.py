def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    words = txt.split(" ")
    last_char = txt.charAt(txt.length - 1)

    if words.length == 0 || last_char!~ /[a-zA-Z]/
        return false
    else if words.length == 1 && last_char!~ /\w/
        return true
    else if words.length > 1 && last_char!~ /\w/ && words.last.length == 0
        return true
    else
        return false