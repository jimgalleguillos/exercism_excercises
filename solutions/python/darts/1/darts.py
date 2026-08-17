
def score(x, y):
    """ Calculate the score of a single dart in the Dart game.

    Args:
        x (float): A real number for x Cartesian coordinates.
        y (float): A real number for y Cartesian coordinates.

    Returns:
        int: The Dart game score.
    """
    dart_distance = (x**2 + y**2) ** 0.5
    if dart_distance <= 1:
        return 10
    if dart_distance > 1 and dart_distance <= 5:
        return 5
    if dart_distance > 5 and dart_distance <= 10:
        return 1
    return 0