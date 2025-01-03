def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    result = []
    if not lst:
        return result

    min_val = min(lst)
    result.append(min_val)
    lst.remove(min_val)

    if not lst:
        return result

    max_val = max(lst)
    result.append(max_val)
    lst.remove(max_val)

    if not lst:
        return result

    while lst:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)

        if not lst:
            return result

        max_val = max(lst)
        result.append(max_val)
        lst.remove(max_val)

        if not lst:
            return result
    ```
    This Kotlin function `strange_sort_list` takes a list of integers as input and returns a list in strange order. The function follows the same logic as the provided Python function.

    Note:
    - The function uses list comprehension to find the minimum and maximum values in the input list.
    - The function handles empty input list.

    Hint:
    - You can use a while loop to iterate through the list.
    - Use `remove` method to remove elements from the list.
    - Use `min` and `max` functions to find minimum and maximum values.
    - Return the final sorted list.

    Example usage:
    ```
    val lst = listOf(1, 2, 3, 4, 5, 5, 5, 5)
    println(strange_sort_list(lst))
    ```
    Output:
    ```
    [1, 5, 2, 3, 4, 5, 5, 5]
    ```

    Note:
    - The function is not optimized for large lists.
    - The function may not work correctly if the input list contains negative integers.

    You can improve the function by adding appropriate error handling and optimizing it for large lists.
    */
    return lst.sorted()