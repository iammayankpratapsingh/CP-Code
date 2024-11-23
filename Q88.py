def solveMaze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

    def solve(x, y, path):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            path.append((x, y))
            return True
        if is_valid(x, y):
            path.append((x, y))
            maze[x][y] = 0
            if solve(x + 1, y, path) or solve(x, y + 1, path):
                return True
            path.pop()
            maze[x][y] = 1
        return False

    path = []
    if solve(0, 0, path):
        return path
    return []

print(solveMaze([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]))
