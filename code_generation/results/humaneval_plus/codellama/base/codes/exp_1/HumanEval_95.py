def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    if not isinstance(dict, dict):
        return False
    if not all(isinstance(key, str) for key in dict.keys()):
        return False
    if not all(isinstance(value, str) for value in dict.values()):
        return False
    if not all(value.isupper() or value.islower() for value in dict.values()):
        return False
    if not all(key.isupper() or key.islower() for key in dict.keys()):
        return False
    return True