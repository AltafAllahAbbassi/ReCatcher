def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    if k == len(arr):
        return sorted(arr)
    if k == 1:
        return [max(arr)]
    if k == len(arr) - 1:
        return sorted(arr, reverse=True)
    if k == 2:
        return sorted(arr, reverse=True)[:2]

    # 1. Find the maximum element in the array
    max_element = max(arr)

    # 2. Create a new array with the maximum element at the beginning
    new_arr = [max_element]

    # 3. Find the second maximum element in the array
    arr.remove(max_element)
    second_max_element = max(arr)

    # 4. Create a new array with the second maximum element at the beginning
    new_arr.append(second_max_element)

    # 5. Find the third maximum element in the array
    arr.remove(second_max_element)
    third_max_element = max(arr)

    # 6. Create a new array with the third maximum element at the beginning
    new_arr.append(third_max_element)

    # 7. Find the fourth maximum element in the array
    arr.remove(third_max_element)
    fourth_max_element = max(arr)

    # 8. Create a new array with the fourth maximum element at the beginning
    new_arr.append(fourth_max_element)

    # 9. Find the fifth maximum element in the array
    arr.remove(fourth_max_element)
    fifth_max_element = max(arr)

    # 10. Create a new array with the fifth maximum element at the beginning
    new_arr.append(fifth_max_element)

    # 11. Find the sixth maximum element in the array
    arr.remove(fifth_max_element)
    sixth_max_element = max(arr)

    # 12. Create a new array with the sixth maximum element at the beginning
    new_arr.append(sixth_max_element)

    # 13. Find the seventh maximum element in the array
    arr.remove(sixth_max_element)
    seventh_max_element = max(arr)

    # 14. Create a new array with the seventh maximum element at the beginning
    new_arr.append(seventh_max_element)

    # 15. Find the eighth maximum element in the array
    arr.remove(seventh_max_element)
    eighth_max_element = max(arr)

    # 16. Create a new array with the eighth maximum element at the beginning
    new_arr.append(eighth_max_element)

    # 17. Find the ninth maximum element in the array
    arr.remove(eighth_max_element)
    ninth_max_element = max(arr)

    # 18. Create a new array with the ninth maximum element at the beginning
    new_arr.append(ninth_max_element)

    # 19. Find the tenth maximum element in the array
    arr.remove(ninth_max_element)
    tenth_max_element = max(arr)

    # 20. Create a new array with the tenth maximum element at the beginning
    new_arr.append(tenth_max_element)

    # 21. Find the eleventh maximum element in the array
    arr.remove(tenth_max_element)
    eleventh_max_element = max(arr)

    # 22. Create a new array with the eleventh maximum element at the beginning
    new_arr.append(eleventh_max_element)

    # 23. Find the twelfth maximum element in the array
    arr.remove(eleventh_max_element)
    twelfth_max_element = max(arr)

    # 24. Create a new array with the twelfth maximum element at the beginning
    new_arr.append(twelfth_max_element)

    # 25. Find the thirteenth maximum element in the array
    arr.remove(twelfth_max_element)
    thirteenth