def rotate(text, key):
    """This function performs the Caesar cipher.
    
    Input:
    - text: string to be cipher.
    - key: integer between 0-26 for shift the text.

    Output:
    - string: a cipher      string
    """
    if key in {0,26}:
        return text
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enum_abc_lower = {let_index : letter  for letter, let_index in enumerate(abc_lower)}
    enum_abc_upper = {let_index : letter for letter, let_index in enumerate(abc_upper)}
    enum_abc_lower_rev = {letter : let_index for letter, let_index in enumerate(abc_lower)}
    enum_abc_upper_rev = {letter : let_index for letter, let_index in enumerate(abc_upper)}
    result = []
    for char in text:
        if char.islower():
            pos = enum_abc_lower[char]
            new_pos = (pos + key) % 26
            result.append(enum_abc_lower_rev[new_pos])
        elif char.isupper():
            pos = enum_abc_upper[char]
            new_pos = (pos + key) % 26
            result.append(enum_abc_upper_rev[new_pos])
        else:
            result.append(char)
    return "".join(result)