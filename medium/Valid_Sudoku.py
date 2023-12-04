def is_valid_sudoku(board):
    def is_valid_block(block):
        block = [x for x in block if x != '.']
        return len(block) == len(set(block))

    for i in range(9):
        row = [board[i][j] for j in range(9)]
        column = [board[j][i] for j in range(9)]
        if not is_valid_block(row) or not is_valid_block(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_block(block):
                return False

    return True
