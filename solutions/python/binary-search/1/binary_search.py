def find(search_list, value):
    """ Function that applies binary search to find a value in a sorted list.

    Args:
        search_list (list[int]):  The list of numbers being searched.
        value (int): The value that will be sought.

    Raises:
        ValueError: An error is raised if value not in list.

    Returns:
        int: The index of the value in the list.
    """
    left = 0
    right = len(search_list)-1
    while left <= right:
        middle = (left+right)//2
        middle_value = search_list[middle]
        # the value is the middle one
        if middle_value == value:
            return middle
        # the middle value is less than the value
        elif middle_value < value:
            left = middle+1
        # the middle value is greater than the value
        else:
            right = middle-1
    raise ValueError("value not in array")
            
