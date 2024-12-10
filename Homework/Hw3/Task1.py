def find_critical_edges(n, edges):
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    visited = [-1] * n
    lowest_reachable = [float('inf')] * n
    discovery_time = [float('inf')] * n
    parent = [-1] * n
    timer = 0
    critical_edges = []

    def dfs(node):
        nonlocal timer
        visited[node] = discovery_time[node] = lowest_reachable[node] = timer
        timer += 1

        for u in graph[node]:
            if visited[u] == -1:
                parent[u] = node
                dfs(u)
                lowest_reachable[node] = min(lowest_reachable[node], lowest_reachable[u])
                if lowest_reachable[u] > discovery_time[node]:
                    critical_edges.append([node, u])
            elif u != parent[node]:
                lowest_reachable[node] = min(lowest_reachable[node], discovery_time[u])

    for v in range(n):
        if visited[v] == -1:
            dfs(v)

    return critical_edges


# Тестирование
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
result_critical_edges = find_critical_edges(n, connections)
print(f"Critical Edges: {result_critical_edges}")  # Должно быть: [[1, 3]]