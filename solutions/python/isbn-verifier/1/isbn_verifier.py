def is_valid(isbn):
    """ This function checks whether the ISBN-10 string is used to validate book identification numbers.

    Input:
    - isbn: String to be checked.
    
    Output:
    - boolean: True if it is a valid ISBN-10.
    """
    if not isbn: # Empty string
        return False
    short_isbn = isbn.replace("-","").lower()
    if len(short_isbn) != 10: # ISBN-10 need 10 digits
        return False
    if not short_isbn[0:9].isdigit(): # Check if 0 to 9 elements are digit.
        return False
    if not short_isbn[-1].isdigit(): # Check if last element are digit or X
        if short_isbn[-1] != "x":
            return False
    isbn_check = 0
    mult_counter = 10
    for dig in short_isbn:
        if dig == "x":
            isbn_check += 10 * mult_counter
        else:
            isbn_check += int(dig) * mult_counter
        mult_counter -= 1
    return isbn_check % 11 == 0
    