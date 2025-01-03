from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maximums = []
    for i, number in enumerate(numbers):
        if i == 0:
            rolling_maximums.append(number)
        else:
            rolling_maximums.append(max(rolling_maximums[i - 1], number))
    return rolling_maximums