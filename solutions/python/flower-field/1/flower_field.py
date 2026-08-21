POSITIONS = [ # positions surrounding the flower
    (-1,-1),(0,-1),(1,-1), # top positions
    (1,0),(-1,0), # middle positions
    (-1,1),(0,1),(1,1) # bot positions
]

def annotate(garden):
    """ This takes a garden board and replaces its empty spaces with the number of flowers surrounding that empty space.

    Args:
        garden (list[str]): The list containing the garden elements.

    Raises:
        ValueError: An error occurs when the garden board is invalid.

    Returns:
        list[str]: It returns the same garden board, but with the number of flowers surrounding the empty spaces.
    """
    if any(not elem for elem in garden):
        return garden
    mut_garden = [list(row)for row in garden]
    # different row length
    if len(mut_garden)>1:
        for row_index in range(len(mut_garden)-1):
            if len(mut_garden[row_index]) != len(mut_garden[row_index+1]):
                raise ValueError("The board is invalid with current input.")
    for row_index, row in enumerate(mut_garden):
        for col_index, elem in enumerate(row):
            if elem not in {" ", "*"}:
                raise ValueError("The board is invalid with current input.")
            count = 0

            # check if elem is not a flower.
            if elem == " ":
                for px,py in POSITIONS:
                    dx = px + col_index
                    dy = py + row_index
                    if 0 <= dx < len(row) and 0 <= dy < len(mut_garden):
                        if mut_garden[dy][dx] == "*":
                            count += 1
            # replace the empty space 
            if count > 0:
                mut_garden[row_index][col_index] = str(count)
    return ["".join(row) for row in mut_garden]
            
                            
                        
                    
                
            
                
        
            
                