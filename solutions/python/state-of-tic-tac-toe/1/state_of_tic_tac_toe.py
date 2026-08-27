def gamestate(board):
    """Given a tic-tac-toe board, check if there is a winner.

    Args:
        board (list[str]): A list that simulates a 3x3 board. The length of the list and the strings is three.

    Raises:
        ValueError: Wrong turn order: O started
        ValueError: Wrong turn order: X went twice
        ValueError: Impossible board: game should have ended after the game was won

    Returns:
        str: The board status, check if there is a winner. values can be (win,ongoing,draw)
    """
    board_string = "".join(board)
    # count x
    x_count = board_string.count("X")
    # count o
    o_count = board_string.count("O")
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    b_grid = [list(row) for row in board]
    # winning moves
    grid_game_state = [
        b_grid[0],
        b_grid[1],
        b_grid[2],  # rows
        [b_grid[0][0], b_grid[1][0], b_grid[2][0]],  # columns
        [b_grid[0][1], b_grid[1][1], b_grid[2][1]],
        [b_grid[0][2], b_grid[1][2], b_grid[2][2]],
        [b_grid[0][0], b_grid[1][1], b_grid[2][2]],  # diagonals
        [b_grid[0][2], b_grid[1][1], b_grid[2][0]],
    ]

    # search winners plays
    game_list = []
    x_status = False
    o_status = False

    for elem in grid_game_state:
        result = set(elem)
        if result == {"X"}:
            x_status = True
        if result == {"O"}:
            o_status = True
        game_list.append(result)

    # check winners
    # there cannot be two winners.
    if x_status and o_status:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
    # have 1 winner
    if x_status or o_status:
        return "win"
    # match in progress
    for aling_result in game_list:
        if " " in aling_result:
            return "ongoing"
    # the grid is full, draw
    return "draw"