def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a == b:
            return None
        elif float(a.replace(',', '.')) > float(b.replace(',', '.')):
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        if float(a) > float(b.replace(',', '.')):
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        if float(a.replace(',', '.')) > float(b):
            return a
        else:
            return b