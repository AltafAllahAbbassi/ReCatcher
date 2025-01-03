def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    if len(lst)!= 2:
        return 'Invalid input'

    str1 = lst[0]
    str2 = lst[1]

    if not str1 or not str2:
        return 'Invalid input'

    if len(str1)!= len(str2):
        return 'No'

    for char in str1:
        if char == '(':
            count_open = count_open + 1
        elif char == ')':
            count_close = count_close + 1

    if count_open!= count_close:
        return 'No'

    return 'Yes'