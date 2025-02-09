def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # replace all consecutive underscores with -
    while '__' in text:
        text = text.replace('__', '-')
    
    # if the first character is an underscore, remove it
    if text[0] == '_':
        text = text[1:]
    
    # if the last character is an underscore, remove it
    if text[-1] == '_':
        text = text[:-1]
    
    return text