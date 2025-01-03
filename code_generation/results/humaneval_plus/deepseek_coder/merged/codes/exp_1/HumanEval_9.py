from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = numbers[0]
    result = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        result.append(max_num)
    return result