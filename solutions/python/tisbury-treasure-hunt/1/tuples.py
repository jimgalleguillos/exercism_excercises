"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    coords = tuple(coordinate)
    return coords


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    azara_coords = azara_record[1]
    rui_coords = rui_record[1]
    if isinstance(azara_coords, str):
        azara_coords = convert_coordinate(azara_coords)
    if isinstance(rui_coords, str):
        rui_coords = convert_coordinate(rui_coords)
    if azara_coords == rui_coords:
        return True
    return False


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if not compare_records(azara_record, rui_record):
        return "not a match"
    return azara_record + rui_record

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    lines = []
    for elem in combined_record_group:
        name = elem[0]
        place = elem[2]
        coords = elem[3]
        color = elem[4]
        record = str((name, place, coords, color))
        lines.append(record)
    cleaned_records = ""
    for line in lines:
        cleaned_records += line + "\n"
    return cleaned_records
        
        
