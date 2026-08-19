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
def value(colors):
    """ Returns the first two resistors codes using his names.

    Args:
        colors (list[str]): A list with color names.

    Returns:
        int: The first two resistor codes.
    """
    color_values = []
    color_values.append(str(RESISTOR_COLORS.index(colors[0])))
    color_values.append(str(RESISTOR_COLORS.index(colors[1])))
    return int("".join(color_values))
