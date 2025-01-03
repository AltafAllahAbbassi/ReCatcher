def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # your code here
    if len(file_name) < 3:
        return 'No'
    if file_name.count('.')!= 1:
        return 'No'
    if file_name.find('.') == 0:
        return 'No'
    if file_name.find('.') == len(file_name) - 1:
        return 'No'
    if file_name.find('.') == len(file_name) - 2:
        return 'No'
    if file_name.find('.') == len(file_name) - 3:
        return 'No'
    if file_name.find('.') == len(file_name) - 4:
        return 'No'
    if file_name.find('.') == len(file_name) - 5:
        return 'No'
    if file_name.find('.') == len(file_name) - 6:
        return 'No'
    if file_name.find('.') == len(file_name) - 7:
        return 'No'
    if file_name.find('.') == len(file_name) - 8:
        return 'No'
    if file_name.find('.') == len(file_name) - 9:
        return 'No'
    if file_name.find('.') == len(file_name) - 10:
        return 'No'
    if file_name.find('.') == len(file_name) - 11:
        return 'No'
    if file_name.find('.') == len(file_name) - 12:
        return 'No'
    if file_name.find('.') == len(file_name) - 13:
        return 'No'
    if file_name.find('.') == len(file_name) - 14:
        return 'No'
    if file_name.find('.') == len(file_name) - 15:
        return 'No'
    if file_name.find('.') == len(file_name) - 16:
        return 'No'
    if file_name.find('.') == len(file_name) - 17:
        return 'No'
    if file_name.find('.') == len(file_name) - 18:
        return 'No'
    if file_name.find('.') == len(file_name) - 19:
        return 'No'
    if file_name.find('.') == len(file_name) - 20:
        return 'No'
    if file_name.find('.') == len(file_name) - 21:
        return 'No'
    if file_name.find('.') == len(file_name) - 22:
        return 'No'
    if file_name.find('.') == len(file_name) - 23:
        return 'No'
    if file_name.find('.') == len(file_name) - 24:
        return 'No'
    if file_name.find('.') == len(file_name) - 25:
        return 'No'
    if file_name.find('.') == len(file_name) - 26:
        return 'No'
    if file_name.find('.') == len(file_name) - 27:
        return 'No'
    if file_name.find('.') == len(file_name) - 28:
        return 'No'
    if file_name.find('.') == len(file_name) - 29:
        return 'No'
    if file_name.find('.') == len(file_name) - 30:
        return 'No'
    if file_name.find('.') == len(file_name) - 31:
        return 'No'
    if file_name.find('.') == len(file_name) - 32:
        return 'No'
    if file_name.find('.') == len(file_name) - 33:
        return 'No'
    if file_name.find('.') == len(file_name) - 34:
        return 'No'
    if file_name.find('.') == len(file_name) -