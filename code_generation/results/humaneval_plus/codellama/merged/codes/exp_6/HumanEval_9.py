from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements = []
    for i, num in enumerate(numbers):
        if i == 0:
            max_elements.append(num)
        else:
            max_elements.append(max(num, max_elements[-1]))
    return max_elements