def solveNQueens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def solve(row):
        if row == n:
            result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    board = [-1] * n
    result = []
    solve(0)
    return result

print(solveNQueens(4))
