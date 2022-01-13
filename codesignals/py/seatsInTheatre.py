def seatsInTheater(nCols, nRows, col, row):
    behind = nCols - col + 1
    side = nRows - row
    return behind * side