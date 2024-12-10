from collections import deque

class Network:
    def __init__(self, size):
        self.size = size
        self.capacity = [[0] * size for _ in range(size)]

    def add_edge(self, u, v, cap):
        self.capacity[u][v] += cap

    def get_capacity(self, u, v):
        return self.capacity[u][v]

def bfs(graph, flow, source, sink, parent):
    visited = [False] * graph.size
    queue = deque([source])
    visited[source] = True

    while queue:
        current = queue.popleft()
        if current == sink:
            return True

        for u in range(graph.size):
            if not visited[u] and graph.get_capacity(current, u) > flow.get_capacity(current, u):
                visited[u] = True
                parent[u] = current
                queue.append(u)
                if u == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    flow = Network(graph.size)
    total_flow = 0
    parent = [-1] * graph.size

    while bfs(graph, flow, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph.get_capacity(parent[s], s) - flow.get_capacity(parent[s], s))
            s = parent[s]
        
        v = sink
        while v != source:
            flow.add_edge(parent[v], v, path_flow)
            flow.add_edge(v, parent[v], -path_flow)
            v = parent[v]
        
        total_flow += path_flow

    return total_flow

def create_network(num_people, num_teas):
    network = Network(num_people + num_teas + 2)
    total_guess = 0

    for tea in range(1, num_teas + 1):
        count = int(input())
        total_guess += count
        network.add_edge(0, tea, count)

    total_guess //= num_people

    for person in range(1, num_people + 1):
        count = int(input())
        for _ in range(count):
            tea_choice = int(input())
            network.add_edge(tea_choice, num_teas + person, float('Inf'))

    return network, total_guess

def max_days_possible(graph, num_people, num_teas, max_guess):
    capacity_copy = Network(graph.size)
    capacity_copy.capacity = [row[:] for row in graph.capacity]
    
    left, right = 0, max_guess + 1
    
    while right - left > 1:
        mid = (right + left) // 2
        for person in range(1, num_people + 1):
            capacity_copy.add_edge(num_teas + person, num_teas + num_people + 1, mid)

        if edmonds_karp(capacity_copy, 0, num_teas + num_people + 1) == mid * num_people:
            left = mid
        else:
            right = mid
            
    return left

num_people, num_teas = map(int, input().split())
network_graph, estimated_max_days = create_network(num_people, num_teas)
print("Result =", max_days_possible(network_graph, num_people, num_teas, estimated_max_days))