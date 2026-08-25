def egg_count(display_value):
    """ Calculate the number of eggs ready to be collected. Convert a number into binary, where the 1s represent the eggs to be collected.

    Args:
        display_value (int): The number to be converted to binary.

    Returns:
        int: The number of eggs ready to be collected.
    """
    binaries = []
    # get the binaries from display_value.
    while display_value > 0:
        bin_value = display_value % 2
        binaries.append(bin_value)
        display_value = display_value //2
    binaries = binaries[::-1]
    # get the eggs to be collected from binaries.
    total_eggs = 0
    if binaries:
        for bin_value in binaries:
            total_eggs+=bin_value
    return total_eggs
        