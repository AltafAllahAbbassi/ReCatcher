def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if a > b and a > c:
        if a**2 == b**2 + c**2:
            return True
        else:
            return False
    elif b > a and b > c:
        if b**2 == a**2 + c**2:
            return True
        else:
            return False
    elif c > a and c > b:
        if c**2 == a**2 + b**2:
            return True
        else:
            return False
    else:
        return False