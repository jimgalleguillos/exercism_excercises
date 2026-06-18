def is_paired(input_string):
    braket_stack = []
    open_brackets = {"[":1,"{":2, "(":3}
    close_brackets = {"]":1, "}":2, ")":3}
    for c in input_string:
        if c in open_brackets:
            braket_stack.append(c)
        if c in close_brackets:
            if braket_stack and open_brackets[braket_stack[-1]] == close_brackets[c]:
                braket_stack.pop()
            else:
                return False
    return not braket_stack