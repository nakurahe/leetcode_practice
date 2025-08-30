def isValidSudoku(board: list[list[str]]) -> bool:
    # referred to https://leetcode.com/problems/valid-sudoku/solutions/15472/short-simple-java-using-strings
    n = 9
    record = set()

    for i in range(n):
        for j in range(n):
            if board[i][j] != ".":
                if (
                    (board[i][j] + str(i)) not in record
                    and (str(j) + board[i][j]) not in record
                    and (str(i // 3) + board[i][j] + str(j // 3)) not in record
                ):
                    record.add(board[i][j] + str(i))
                    record.add(str(j) + board[i][j])
                    record.add(str(i // 3) + board[i][j] + str(j // 3))
                else:
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
print(isValidSudoku(board))
