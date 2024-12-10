def has_bidirectional_path(graph: list[list[int]], start: int, end: int) -> bool:
    visited = [0] * len(graph)
    
    def dfs(v: int) -> None:
        visited[v] = 1
        for u in graph[v]:
            if visited[u] != 1:
                dfs(u)

    dfs(start)
    if visited[end] == 1:
        visited = [0] * len(graph)
        dfs(end)
        return visited[start] == 1
    
    return False