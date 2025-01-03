from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    if len(numbers) == 3:
        return numbers[0], numbers[2]
    if len(numbers) == 4:
        return numbers[0], numbers[2]
    if len(numbers) == 5:
        return numbers[0], numbers[2]
    if len(numbers) == 6:
        return numbers[0], numbers[2]
    if len(numbers) == 7:
        return numbers[0], numbers[2]
    if len(numbers) == 8:
        return numbers[0], numbers[2]
    if len(numbers) == 9:
        return numbers[0], numbers[2]
    if len(numbers) == 10:
        return numbers[0], numbers[2]
    if len(numbers) == 11:
        return numbers[0], numbers[2]
    if len(numbers) == 12:
        return numbers[0], numbers[2]
    if len(numbers) == 13:
        return numbers[0], numbers[2]
    if len(numbers) == 14:
        return numbers[0], numbers[2]
    if len(numbers) == 15:
        return numbers[0], numbers[2]
    if len(numbers) == 16:
        return numbers[0], numbers[2]
    if len(numbers) == 17:
        return numbers[0], numbers[2]
    if len(numbers) == 18:
        return numbers[0], numbers[2]
    if len(numbers) == 19:
        return numbers[0], numbers[2]
    if len(numbers) == 20:
        return numbers[0], numbers[2]
    if len(numbers) == 21:
        return numbers[0], numbers[2]
    if len(numbers) == 22:
        return numbers[0], numbers[2]
    if len(numbers) == 23:
        return numbers[0], numbers[2]
    if len(numbers) == 24:
        return numbers[0], numbers[2]
    if len(numbers) == 25:
        return numbers[0], numbers[2]
    if len(numbers) == 26:
        return numbers[0], numbers[2]
    if len(numbers) == 27:
        return numbers[0], numbers[2]
    if len(numbers) == 28:
        return numbers[0], numbers[2]
    if len(numbers) == 29:
        return numbers[0], numbers[2]
    if len(numbers) == 30:
        return numbers[0], numbers[2]
    if len(numbers) == 31:
        return numbers[0], numbers[2]
    if len(numbers) == 32:
        return numbers[0], numbers[2]
    if len(numbers) == 33:
        return numbers[0], numbers[2]
    if len(numbers) == 34:
        return numbers[0], numbers[2]
    if len(numbers) == 35:
        return numbers[0], numbers[2]
    if len(numbers) == 36:
        return numbers[0], numbers[2]
    if len(numbers) == 37:
        return numbers[0], numbers[2]
    if len(numbers) == 38:
        return numbers[0], numbers[2]
    if len(numbers) == 39:
        return numbers[0], numbers[2]
    if len(numbers) == 40:
        return numbers[0], numbers[2]
    if len(numbers) == 41:
        return numbers[0], numbers[2]
    if len(numbers) == 42:
        return numbers[0], numbers[2]
    if len(numbers) == 43:
        return numbers[0], numbers[2]
    if len(numbers) == 44:
        return numbers[0], numbers[2]
    if len(numbers) == 45:
        return numbers[0],