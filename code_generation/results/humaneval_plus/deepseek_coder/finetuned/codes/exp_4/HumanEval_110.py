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
            # Find the first odd number in lst1
            odd_num = num
            break

    for num in lst2:
        if num % 2 == 0:
            # Find the first even number in lst2
            even_num = num
            break

    # Exchange the odd number from lst1 with the even number from lst2
    lst1[lst1.index(odd_num)] = even_num
    lst2[lst2.index(even_num)] = odd_num

    # Check if all elements in lst1 are even now
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"