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
    "white"
]
RESISTOR_TOLERANCE = [
    ("grey","±0.05%"),
    ("violet","±0.1%"),
    ("blue","±0.25%"),
    ("green","±0.5%"),
    ("brown","±1%"),
    ("red","±2%"),
    ("gold","±5%"),
    ("silver","±10%")
]
def resistor_label(colors):
    """ These functions create a label using the color names of three resistors. This indicates the value in ohms and its tolerance value.

    Args:
        colors (list[str]): A list of resistor color names, with the name of the corresponding tolerance in the final position.

    Returns:
        str: Returns the resistors ohms label. This indicates the resistors quantity in ohms and its tolerance value.
    """
    # calculate ohms
    ohms = 0
    # for 1 color
    if len(colors) < 2:
        ohms += RESISTOR_COLORS.index(colors[0])
        return f"{ohms} ohms"
    # for 4,5 colors
    for col_index, color in enumerate(colors[:-2][::-1]):
        ohms += RESISTOR_COLORS.index(color)*10**col_index # base number
    # multiplier
    ohms *= 10**RESISTOR_COLORS.index(colors[-2])
    # quantity label
    ohms = list(str(ohms))
    total_ohms = int("".join(ohms))
    ohms_length = len(ohms)
    if ohms_length < 4:
        formated_value = total_ohms
        unit = "ohms"
    elif 4 <= ohms_length < 7:
        formated_value = total_ohms/1000
        unit = "kiloohms"
    elif 7 <= ohms_length < 10:
        formated_value = total_ohms/1000000
        unit = "megaohms"
    else:
        formated_value = total_ohms/1000000000
        unit = "gigaohms"
    # remove the zero after the decimal point if is a integer value 2.0 to 2
    if isinstance(formated_value, float) and formated_value.is_integer():
        formated_value = int(formated_value)
    # get the tolerance value
    tolerance = dict(RESISTOR_TOLERANCE).get(colors[-1])
    return f"{formated_value} {unit} {tolerance}"
