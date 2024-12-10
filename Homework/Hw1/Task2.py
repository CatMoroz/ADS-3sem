def has_odd_index_cycle(graph: list[list[int]]) -> bool:
    state = [0] * len(graph)
    
    def dfs(v: int) -> bool:
        if v % 2 == 1:
            return False
        state[v] = 1
        for u in graph[v]:
            if state[u] == 1 or (state[u] == 0 and dfs(u)):
                return True
        state[v] = 2
        return False

    for v in range(0, len(graph), 2):
        if state[v] == 0 and dfs(v):
            return True
            
    return False