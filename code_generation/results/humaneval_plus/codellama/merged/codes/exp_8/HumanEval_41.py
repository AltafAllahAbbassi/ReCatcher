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
    left_to_right = range(n)
    right_to_left = range(n - 1, -1, -1)

    collisions = 0
    while True:
        for i in left_to_right:
            if i == n - 1:
                if right_to_left[0] == 0:
                    break
                else:
                    right_to_left = range(n - 1, -1, -1)
            if left_to_right[i] == right_to_left[0]:
                collisions++
                break
        for i in right_to_left:
            if i == 0:
                if left_to_right[n - 1] == n - 1:
                    break
                else:
                    left_to_right = range(n)
            if right_to_left[i] == left_to_right[0]:
                collisions++
                break
    return collisions