ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def rows(letter):
    """ Take the letter and form a diamond shape in conjunction with the preceding letters, following the order of the alphabet.

    Args:
        letter (str): A single letter.

    Returns:
        list[str]: The list of elements that make up the diamond.
    """
    # Only A
    if letter == "A":
        return ["A"]
    
    half_diamond = []
    letter_pos = ALPHABET.index(letter)
    num_middle_spaces = 1
    num_extern_spaces = letter_pos
    target_index = ALPHABET.index(letter)
    for index in range(target_index+1):
        ex_spaces = " " * num_extern_spaces
        lett = ALPHABET[index]
        # letter A
        if index == 0:
            text = ex_spaces + lett + ex_spaces
        # any other letter
        else:
            midd_spaces = " " * num_middle_spaces
            text = ex_spaces + lett + midd_spaces + lett + ex_spaces
            num_middle_spaces += 2
        num_extern_spaces-=1
        half_diamond.append(text)
    end_diamond = half_diamond[:-1]
    diamond = half_diamond + end_diamond[::-1]
    return diamond
