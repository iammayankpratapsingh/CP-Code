def tarjan_bridges(graph):
    def dfs(u, parent):
        nonlocal time
        low[u] = disc[u] = time
        time += 1
        for v in graph[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent:
                low[u] = min(low[u], disc[v])
    
    time = 0
    disc = [-1] * len(graph)
    low = [-1] * len(graph)
    bridges = []
    for u in range(len(graph)):
        if disc[u] == -1:
            dfs(u, -1)
    return bridges

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print(tarjan_bridges(graph))
