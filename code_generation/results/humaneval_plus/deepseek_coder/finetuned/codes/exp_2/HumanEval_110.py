def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Check if all elements in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if it is possible to exchange elements to make all elements even
    for num in lst1:
        if num % 2!= 0:
            # Find the first odd number in lst2
            for i, elem in enumerate(lst2):
                if elem % 2!= 0:
                    # Exchange the odd number with the first odd number in lst1
                    lst1[lst1.index(num)], lst2[i] = lst2[i], num
                    break

    # Check if all elements in lst1 are even after exchange
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"