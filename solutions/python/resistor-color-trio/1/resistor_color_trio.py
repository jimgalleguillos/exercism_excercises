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

def label(colors):
    """ These functions create a label using the color names of three resistors.

    Args:
        colors (list[str]): A list of the color names for three resistors.

    Returns:
        str: Returns the resistors ohms label. 
    """
    f_color = RESISTOR_COLORS.index(colors[0])
    s_color = RESISTOR_COLORS.index(colors[1])
    t_color = RESISTOR_COLORS.index(colors[2])
    ohms = list(str((f_color*10+s_color)*10**t_color))
    ohms_length = len(ohms)
    if ohms_length < 4:
        result = "".join(ohms) + " ohms"
    elif ohms_length >= 4 and ohms_length < 7:
        result = "".join(ohms[:ohms_length-3]) + " kiloohms"
    elif ohms_length >= 7 and ohms_length < 10:
        result = "".join(ohms[:ohms_length-6]) + " megaohms"
    else:
        result = "".join(ohms[:ohms_length-9]) + " gigaohms"
    return result
    