def adjacency_list_to_matrix(adjacency_list: list[list[int]], n: int) -> list[list[int]]:
    adjacency_matrix = [[0] * n for _ in range(n)]
    for v in range(n):
        for u in adjacency_list[v]:
            adjacency_matrix[v][u] = 1
    return adjacency_matrix

def adjacency_list_to_edge_list(adjacency_list: list[list[int]], n: int) -> list[tuple[int, int]]:
    edge_list = []
    for v in range(n):
        for u in adjacency_list[v]:
            edge_list.append((v, u))
    return edge_list

def matrix_to_edge_list(adjacency_matrix: list[list[int]], n: int) -> list[tuple[int, int]]:
    edge_list = []
    for v in range(n):
        for u in range(len(adjacency_matrix[v])):
            if adjacency_matrix[v][u]:
                edge_list.append((v, u))
    return edge_list

def matrix_to_adjacency_list(adjacency_matrix: list[list[int]], n: int) -> list[list[int]]:
    adjacency_list = [[] for _ in range(n)]
    for v in range(n):
        for u in range(len(adjacency_matrix[v])):
            if adjacency_matrix[v][u]:
                adjacency_list[v].append(u)
    return adjacency_list

def edge_list_to_adjacency_list(edge_list: list[tuple[int, int]], n: int) -> list[list[int]]:
    adjacency_list = [[] for _ in range(n)]
    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])
    return adjacency_list

def edge_list_to_matrix(edge_list: list[tuple[int, int]], n: int) -> list[list[int]]:
    adjacency_matrix = [[0] * n for _ in range(n)]
    for edge in edge_list:
        adjacency_matrix[edge[0]][edge[1]] = 1
    return adjacency_matrix