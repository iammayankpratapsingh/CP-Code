def hamiltonianPath(graph):
    def is_valid(v, pos, path):
        if graph[path[pos - 1]][v] == 0:
            return False
        for i in range(pos):
            if path[i] == v:
                return False
        return True

    def solve(pos, path):
        if pos == len(graph):
            return True
        for v in range(1, len(graph)):
            if is_valid(v, pos, path):
                path[pos] = v
                if solve(pos + 1, path):
                    return True
                path[pos] = -1
        return False

    path = [-1] * len(graph)
    path[0] = 0
    if solve(1, path):
        return path
    return []

print(hamiltonianPath([[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]))
