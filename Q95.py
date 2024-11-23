def knightTour(n):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def solve(x, y, move_count):
        if move_count == n * n:
            return True
        for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                board[nx][ny] = move_count
                if solve(nx, ny, move_count + 1):
                    return True
                board[nx][ny] = -1
        return False

    board = [[-1] * n for _ in range(n)]
    board[0][0] = 0
    if solve(0, 0, 1):
        return board
    return []

print(knightTour(5))
