from collections import deque

class FlowNetwork:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_connection(self, start, end, capacity):
        self.add_vertex(start)
        self.add_vertex(end)
        self.adjacency_list[start][end] = capacity

    def edmonds_karp(self, source, sink):
        total_flow = 0
        residual_graph = {node: {neighbor: cap for neighbor, cap in edges.items()} 
                          for node, edges in self.adjacency_list.items()}
        
        while True:
            queue = deque([source])
            parent_map = {source: None}
            visited_nodes = {source}

            path_found = False
            while queue:
                current_node = queue.popleft()
                if current_node == sink:
                    path_found = True
                    break
                for neighbor, capacity in residual_graph.get(current_node, {}).items():
                    if capacity > 0 and neighbor not in visited_nodes:
                        parent_map[neighbor] = current_node
                        visited_nodes.add(neighbor)
                        queue.append(neighbor)

            if not path_found:
                break

            flow_in_path = float('inf')
            node = sink
            while node != source:
                flow_in_path = min(flow_in_path, residual_graph[parent_map[node]][node])
                node = parent_map[node]

            total_flow += flow_in_path
            node = sink
            while node != source:
                prev_node = parent_map[node]
                residual_graph[prev_node][node] -= flow_in_path
                residual_graph[node][prev_node] = residual_graph.get(node, {}).get(prev_node, 0) + flow_in_path
                node = prev_node

        return total_flow

def calculate_min_blocks(grid, alien_cells):
    height, width = len(grid), len(grid[0])
    network = FlowNetwork()
    network.add_vertex("start")
    network.add_vertex("end")

    cell_mapping = {}
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0:
                cell_id = (row, col)
                cell_mapping[cell_id] = cell_id
                network.add_vertex(cell_id)
                if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                    network.add_connection("start", cell_id, 10**9)
                if (row, col) in alien_cells:
                    network.add_connection(cell_id, "end", 10**9)

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0:
                for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + delta_row, col + delta_col
                    if 0 <= new_row < height and 0 <= new_col < width and grid[new_row][new_col] == 0:
                        network.add_connection(cell_mapping[(row, col)], cell_mapping[(new_row, new_col)], 1)

    max_flow_value = network.edmonds_karp("start", "end")
    return max(0, max_flow_value)

# Тестирование:
test_field1 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
alien_positions1 = [(1, 1)]
print(f"Min blocks: {calculate_min_blocks(test_field1, alien_positions1)}") # Output: 4

test_field2 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]
alien_positions2 = [(2, 2), (3, 3)]
print(f"Min blocks: {calculate_min_blocks(test_field2, alien_positions2)}") # Output: 3

test_field3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
alien_positions3 = [(1, 1)]
print(f"Min blocks: {calculate_min_blocks(test_field3, alien_positions3)}") # Output: 4