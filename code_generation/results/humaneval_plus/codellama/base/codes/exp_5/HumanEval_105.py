def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # Your code here
    arr = sorted(arr)
    arr = arr[::-1]
    arr = [str(i) for i in arr]
    arr = [str(i) for i in arr if i in range(1,10)]
    arr = [str(i) for i in arr if i!= '1']
    arr = [str(i) for i in arr if i!= '2']
    arr = [str(i) for i in arr if i!= '3']
    arr = [str(i) for i in arr if i!= '4']
    arr = [str(i) for i in arr if i!= '5']
    arr = [str(i) for i in arr if i!= '6']
    arr = [str(i) for i in arr if i!= '7']
    arr = [str(i) for i in arr if i!= '8']
    arr = [str(i) for i in arr if i!= '9']
    arr = [str(i) for i in arr if i!= '0']
    arr = [str(i) for i in arr if i!= '']
    arr = [str(i) for i in arr if i!='']
    arr = [str(i) for i in arr if i!= 'None']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'NoneType']
    arr = [str(i) for i in arr if i!= 'None