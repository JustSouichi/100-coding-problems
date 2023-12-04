def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    # Determine which rows and columns need to be zeroed
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    # Set matrix elements to zero
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # Set the first row to zero if needed
    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    # Set the first column to zero if needed
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
