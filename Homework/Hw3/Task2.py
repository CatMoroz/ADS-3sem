def total_inform_time(n, head_id, manager, time_to_inform) -> int:
    d = dict()
    
    for index in range(n):
        if manager[index] != -1:
            if manager[index] not in d:
                d[manager[index]] = []
            d[manager[index]].append(index)

    def dfs(node):
        max_time = 0
        for subordinate in d.get(node, []):
            max_time = max(max_time, dfs(subordinate) + time_to_inform[node])
        return max_time

    return dfs(head_id)