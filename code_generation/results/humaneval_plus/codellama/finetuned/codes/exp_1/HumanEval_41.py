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

    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                cars_left = [i]
            else:
                cars_left.append(i)
        else:
            if i == 0:
                cars_right = [i]
            else:
                cars_right.append(i)

    while True:
        for i in range(n):
            if i % 2 == 0:
                cars_left[i] -= 1
            else:
                cars_right[i] -= 1

            if cars_left[i] == 0:
                collisions += 1
                cars_left[i] = 1000000000

            if cars_right[i] == 0:
                collisions += 1
                cars_right[i] = 1000000000

        if all(x == 1000000000 for x in cars_left) and all(x == 1000000000 for x in cars_right):
            break

    return collisions