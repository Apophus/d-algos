def bishopAndPawn(bishop, pawn):
    columns = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

    bishop_column, bishop_row = int(columns[bishop[0]]), int(bishop[1])
 
    pawn_column, pawn_row = int(columns[pawn[0]]), int(pawn[1])
     
    # gradient == 1
    dx = bishop_row - pawn_row
    dy = bishop_column - pawn_column
    print('bishop:', bishop, 'pawn:', pawn, 'dx:', dx, 'dy:', dy)
    if dx == 0 or dy == 0:
        return False
    elif (dx/dy) == 1 or (dx/dy) == -1:
        return True
    else:
       return False