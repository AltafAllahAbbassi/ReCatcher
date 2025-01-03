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
    cars_left = list(range(n))
    cars_right = list(range(n))
    collisions = 0

    while True:
        for i in range(n):
            if cars_left[i] == cars_right[-(i + 1)]:
                collisions += 1
                print(f"Collision occurred at position {cars_left[i]}")

        for i in range(n):
            cars_left[i] += 1
            cars_right[-(i + 1)] -= 1

        if all(car >= 1000 for car in cars_left) and all(car <= -1000 for car in cars_right):
            break

    return collisions