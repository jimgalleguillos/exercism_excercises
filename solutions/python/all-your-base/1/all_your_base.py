def rebase(input_base, digits, output_base):
    """ Converts a sequence of digits in one base representing a number into a sequence of digits in another base representing the same number.

    Args:
        input_base (int): The input base to rebase.
        digits (list[int]): The list of digits that satisfy the initial base.
        output_base (int): The base to which the change is being made.

    Raises:
        ValueError: input base must be >= 2.
        ValueError: output base must be >= 2.
        ValueError: all digits must satisfy 0 <= d < input base.

    Returns:
        list[int]: The list of numbers that satisfy the base change
    """
    # input base exception
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    # output_base exception
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    # digits exception
    if any(dig < 0 or dig >= input_base for dig in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    # void list
    if not digits:
        return [0]
    # calculate the number
    number = 0
    for index, dig in enumerate(reversed(digits)):
        number += dig*(input_base**index)
    # convert to output base
    new_digits = []
    done = False
    while not done:
        div = number//output_base
        remainder = number%output_base
        number = div
        new_digits.append(remainder)
        if div == 0:
            done = True
    return new_digits[::-1]