def list_sm_to_matrix_sm(list_sm:list[list[int]], n: int) -> list[list[int]]:
    matrix_sm = [[0] for _ in range(n)]
    for i in n:
        for j in list_sm[i]:
            matrix_sm[i][j] = 1
    return matrix_sm

def list_sm_to_list_edge(list_sm:list[list[int]], n: int) -> list[tuple[int, int]]:
    list_edge = []
    for i in n:
        for j in list_sm[i]:
            list_edge.append((i, j))
    return list_edge

def matrix_sm_to_list_edge(matrix_sm:list[list[int]], n: int) -> list[tuple[int, int]]:
    list_edge = []
    for i in range(n):
        for j in range(len(matrix_sm[i])):
            if j:
                list_edge.append((i, j))
    return list_edge

def matrix_sm_to_list_sm(matrix_sm:list[list[int]], n: int) -> list[list[int]]:
    list_sm = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(matrix_sm[i])):
            if j:
                list_sm[i].append(j)
    return list_sm

def list_edge_to_list_sm(list_edge:list[tuple[int, int]], n: int) -> list[list[int]]:
    list_sm = [[] for _ in range(n)]
    for edge in list_edge:
        list_sm[edge[0]].append(edge[1])
    return list_sm

def list_edge_to_matrix_sm(list_edge:list[tuple[int, int]], n: int) -> list[list[int]]:
    matrix_sm = [[0] for _ in range(n)]
    for edge in list_edge:
        matrix_sm[edge[0]][edge[1]] = 1
    return matrix_sm