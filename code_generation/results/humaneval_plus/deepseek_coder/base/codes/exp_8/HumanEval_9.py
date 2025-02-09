from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maximum = []
    for i, number in enumerate(numbers):
        if i == 0:
            rolling_maximum.append(number)
        else:
            rolling_maximum.append(max(rolling_maximum[i - 1], number))
    return rolling_maximum