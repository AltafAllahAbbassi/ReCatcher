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

    You can test the function by calling it with different input lists.

    ```
    println(strange_sort_list(listOf(1, 2, 3, 4)))
    // Output: [1, 4, 2, 3]

    println(strange_sort_list(listOf(5, 5, 5, 5)))
    // Output: [5, 5, 5, 5]

    println(strange_sort_list(emptyList()))
    // Output: []
    ```

    The Kotlin function `strange_sort_list` is equivalent to the provided Python function `strange_sort_list`. You can test the function with different input lists as shown in the example.

    You can find the Kotlin function `strange_sort_list` in the Kotlin version of the code.