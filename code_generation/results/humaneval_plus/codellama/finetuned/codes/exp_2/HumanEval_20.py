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
        raise ValueError("The list of numbers must have at least two elements.")

    closest_pair = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if closest_pair is None or abs(numbers[i] - numbers[j]) < abs(closest_pair[0] - closest_pair[1]):
                closest_pair = (numbers[i], numbers[j])

    return closest_pair