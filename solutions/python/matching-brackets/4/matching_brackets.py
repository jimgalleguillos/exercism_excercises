def is_paired(input_string):
    """ Function that checks if the text is balanced in terms of brackets, parentheses, and braces. """
    bracket_stack = []
    open_brackets = {"[":1,"{":2, "(":3}
    close_brackets = {"]":1, "}":2, ")":3}
    for char in input_string:
        if char in open_brackets:
            bracket_stack.append(char)
        if char in close_brackets:
            if bracket_stack and open_brackets[bracket_stack[-1]] == close_brackets[char]:
                bracket_stack.pop()
            else:
                return False
    return not bracket_stack