def edge_list_to_adjacency_list(edge_list: list[tuple[int, int]], n: int) -> list[list[int]]:
    adjacency_list = [[] for _ in range(n)]
    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])
    return adjacency_list

def topological_order(edge_list: list[tuple[int, int]], total_nodes: int) -> list[int]:
    adjacency_list = edge_list_to_adjacency_list(edge_list, total_nodes)
    visited = [0] * total_nodes
    sorted_nodes = []

    def dfs(node: int):
        visited[node] = 1  
        for u in adjacency_list[node]:
            if visited[u] == 0:
                dfs(u)
        sorted_nodes.append(node)

    for v in range(total_nodes):
        if visited[v] == 0:
            dfs(v)

    sorted_nodes.reverse()
    return sorted_nodes

clothing_dict = {
    0: 'Пиджак', 
    1: 'Часы', 
    2: 'Брюки', 
    3: 'Рубашка', 
    4: 'Трусы', 
    5: 'Носки', 
    6: 'Туфли', 
    7: 'Галстук', 
    8: 'Ремень'
}

edge_list = [
    (7, 0), (5, 6), (3, 8), (3, 7),
    (8, 0), (4, 2), (4, 6), (2, 6),
    (2, 8)
]

result = topological_order(edge_list, 9)

for item in result:
    print(clothing_dict[item])