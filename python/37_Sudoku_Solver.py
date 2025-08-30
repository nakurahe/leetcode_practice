# refer to https://leetcode.com/problems/sudoku-solver/solutions/15752/straight-forward-java-solution-using-backtracking

def isValid(row: int, col: int, char) -> bool:
    for i in range(9):
        if board[row][i] == char:
            return False
        if board[i][col] == char:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
            return False

    return True

def isSolved(board: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for c in range(9):
                    char = str(c + 1)
                    if isValid(i, j, char):
                        board[i][j] = char

                        if isSolved(board):
                            return True
                        else:
                            board[i][j] = "."

                return False

    return True

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

isSolved(board)
print(board)
