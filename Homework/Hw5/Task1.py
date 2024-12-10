def floyd_warshall_with_paths(adjacency_matrix):
    node_count = len(adjacency_matrix)
    distance_matrix = [[float('inf')] * node_count for _ in range(node_count)]
    predecessor_matrix = [[-1] * node_count for _ in range(node_count)]

    for i in range(node_count):
        distance_matrix[i][i] = 0
        for j in range(node_count):
            if adjacency_matrix[i][j] != float('inf'):
                distance_matrix[i][j] = adjacency_matrix[i][j]
                predecessor_matrix[i][j] = i

    for intermediate in range(node_count):
        for start in range(node_count):
            for end in range(node_count):
                if (distance_matrix[start][intermediate] != float('inf') and 
                    distance_matrix[intermediate][end] != float('inf') and 
                    distance_matrix[start][intermediate] + distance_matrix[intermediate][end] < distance_matrix[start][end]):
                    distance_matrix[start][end] = distance_matrix[start][intermediate] + distance_matrix[intermediate][end]
                    predecessor_matrix[start][end] = predecessor_matrix[intermediate][end]

    return distance_matrix, predecessor_matrix


def retrieve_shortest_path(predecessor_matrix, start_node, end_node):
    path_sequence = []
    if predecessor_matrix[start_node][end_node] == -1 and start_node != end_node:
        return None

    current_node = end_node
    while current_node != start_node:
        path_sequence.insert(0, current_node)
        current_node = predecessor_matrix[start_node][current_node]
    path_sequence.insert(0, start_node)
    return path_sequence


# Тестирование
test_graph = [
    [0, 3, float('inf'), float('inf'), 5],
    [3, 0, 1, float('inf'), float('inf')],
    [float('inf'), 1, 0, 7, float('inf')],
    [float('inf'), float('inf'), 7, 0, 2],
    [5, float('inf'), float('inf'), 2, 0]
]

distance_results, predecessor_results = floyd_warshall_with_paths(test_graph)

start_v = 0
end_v = 3

shortest_route = retrieve_shortest_path(predecessor_results, start_v, end_v)

if shortest_route:
    print(f"Shortest path from {start_v} to {end_v}: {shortest_route}")
else:
    print(f"No path exists between {start_v} and {end_v}") # Должно быть: [0, 4, 3]