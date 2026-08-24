ACTIONS = [ # The list with the secret actions
    "wink", #00001
    "double blink", #00010
    "close your eyes", #00100
    "jump", #01000
    "reverse" #10000
]


def commands(binary_str):
    """ Converts a binary into a sequence of secret handshake protocol actions.

    Args:
        binary_str (str): A 5-character binary string

    Returns:
        list[str]: The list with the secret handshake actions.
    """
    mut_binary = list(binary_str)
    result = []
    action = ""
    for value_index, value in enumerate(mut_binary[::-1]):
        binary = int(value)
        if binary:
            action = ACTIONS[value_index]
        if action:
            if action == "reverse":
                result = result[::-1]
            else:
                result.append(action)
            action = ""
    return result