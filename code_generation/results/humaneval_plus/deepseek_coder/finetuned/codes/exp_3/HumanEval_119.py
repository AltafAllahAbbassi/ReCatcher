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
    str1 = lst[0]
    str2 = lst[1]

    # Check if it is possible to concatenate the two strings
    if '(' in str1 and ')' in str2:
        return 'Yes'
    elif '(' in str2 and ')' in str1:
        return 'Yes'
    else:
        return 'No'