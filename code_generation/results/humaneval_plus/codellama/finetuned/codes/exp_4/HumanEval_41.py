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
    collisions = 0

    # Initialize the positions of the cars
    cars_left = [0] * n
    cars_right = [0] * n

    # Start moving the cars
    for i in range(n):
        cars_left[i] = i
        cars_right[i] = -i

    # Continue moving the cars infinitely
    while True:
        for i in range(n):
            if cars_left[i] >= 0 and cars_right[i] <= 0:
                collisions += 1
            cars_left[i] -= 1
            cars_right[i] += 1

    return collisions