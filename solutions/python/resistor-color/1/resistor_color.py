RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def color_code(color):
    """ Returns the color code from color name.

    Args:
        color (str): The color name.

    Returns:
        int: The color code.
    """
    return RESISTOR_COLORS.index(color)


def colors():
    """ Return all color names.

    Returns:
        list[str]: The list with color names.
    """
    return RESISTOR_COLORS
