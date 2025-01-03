def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    brackets = list(string)
    nested = False

    for i in range(len(brackets)):
        if brackets[i] == '[':
            nested = True
        elif brackets[i] == ']':
            nested = False

        if nested and i > 0 and brackets[i - 1] == '[' and (i == 1 or brackets[i - 2]!= ']'):
            return True
    return False