def graphColoring(graph, m):
    def is_valid(node, color, color_assignments):
        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1 and color_assignments[neighbor] == color:
                return False
        return True

    def solve(node, color_assignments):
        if node == len(graph):
            return True
        for color in range(1, m + 1):
            if is_valid(node, color, color_assignments):
                color_assignments[node] = color
                if solve(node + 1, color_assignments):
                    return True
                color_assignments[node] = 0
        return False

    color_assignments = [0] * len(graph)
    if solve(0, color_assignments):
        return color_assignments
    return []

print(graphColoring([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 3))
