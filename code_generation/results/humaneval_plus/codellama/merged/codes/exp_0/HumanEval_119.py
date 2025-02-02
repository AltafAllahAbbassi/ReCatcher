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

    s1 = lst[0]
    s2 = lst[1]

    if not s1 or not s2:
        return 'Invalid input'

    if s1 == s2:
        return 'No'

    if s1[0] == '(' and s2[-1] == ')':
        return 'Yes'

    if s1[-1] == '(' and s2[0] == ')':
        return 'Yes'

    return 'No'