# Solution 1
def revealMinesweeper(board, row, column):
    # O(n * m) time / O(n * m) space; n = number of rows, m = number of columns
    if board[row][column] == 'M':
        board[row][column] = 'X'
    else:
        revealMinesweeperHelper(board, row, column)
    return board

def revealMinesweeperHelper(board, row, column):
    if row not in range(0, len(board)) or column not in range(0, len(board[row])):
        return

    mines = getMinesCount(board, row, column)
    if board[row][column] == 'H' and mines > 0:
        board[row][column] = str(mines)
    elif board[row][column] == 'H' and mines == 0:
        board[row][column] = str(mines)
        revealMinesweeperHelper(board, row - 1, column)
        revealMinesweeperHelper(board, row - 1, column - 1)
        revealMinesweeperHelper(board, row, column - 1)
        revealMinesweeperHelper(board, row + 1, column - 1)
        revealMinesweeperHelper(board, row + 1, column)
        revealMinesweeperHelper(board, row + 1, column + 1)
        revealMinesweeperHelper(board, row, column + 1)
        revealMinesweeperHelper(board, row - 1, column + 1)
    elif board[row][column] == 'M':
        board[row][column] = 'X'
    else:
        return

def getMinesCount(board, row, column):
    mines = 0
    mines += isMine(board, row - 1, column)
    mines += isMine(board, row - 1, column - 1)
    mines += isMine(board, row, column - 1)
    mines += isMine(board, row + 1, column - 1)
    mines += isMine(board, row + 1, column)
    mines += isMine(board, row + 1, column + 1)
    mines += isMine(board, row, column + 1)
    mines += isMine(board, row - 1, column + 1)
    return mines

def isMine(board, row, column):
    if row not in range(0, len(board)) or column not in range(0, len(board[row])):
        return 0
    elif board[row][column] == 'M':
        return 1
    else:
        return 0

print(revealMinesweeper([
    ["M", "M"],
    ["H", "H"],
    ["H", "H"]
], 2, 0
))
