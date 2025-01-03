def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    left_to_right = set(range(n))
    right_to_left = set(range(n))

    collisions = 0
    while left_to_right and right_to_left:
        if min(left_to_right) < min(right_to_left):
            car = min(left_to_right)
            left_to_right.remove(car)
            car = min(right_to_left)
            right_to_left.remove(car)
            collisions++
        else:
            car = min(right_to_left)
            right_to_left.remove(car)
            car = min(left_to_right)
            left_to_right.remove(car)
            collisions++

    return collisions