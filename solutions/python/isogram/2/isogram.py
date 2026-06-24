def is_isogram(string):
    """ This function checks whether a word or phrase is an isogram.

    Input:
    - string: string to be checked.

    Output:
    - boolean: True if it is a isogram.
    """
    isogram_set_check = set()
    for symbol in string.lower():
        if symbol in {" ", "-"}: # It ignores whether it is a hyphen or a space
            continue
        if symbol not in isogram_set_check:
            isogram_set_check.add(symbol)
        else:
            return False
    return True
        
        
