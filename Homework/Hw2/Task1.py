def topological_sort(adjacency_list: list[list[int]], num_nodes: int):
    visited = [0] * num_nodes
    node_queue = list(range(num_nodes))
    sorted_result = []

    while node_queue:
        v = node_queue[0]
        
        if visited[v]:
            node_queue.pop(0)
            continue
        
        if all(visited[u] for u in adjacency_list[v]):
            visited[v] = 1
            sorted_result.insert(0, node_queue.pop(0))
        else:
            node_queue = adjacency_list[v] + node_queue

    return sorted_result