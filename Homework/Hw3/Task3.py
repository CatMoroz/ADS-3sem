from collections import defaultdict

def identify_strongly_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    stack = []
    discovery_index = [0] * n
    lowlink_value = [0] * n
    index_counter = 0
    scc_list = []

    def dfs(v):
        nonlocal index_counter, scc_list
        discovery_index[v] = lowlink_value[v] = index_counter
        index_counter += 1
        stack.append(v)
        visited[v] = True
        
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
                lowlink_value[v] = min(lowlink_value[v], lowlink_value[u])
            elif u in stack:
                lowlink_value[v] = min(lowlink_value[v], discovery_index[u])
        
        if discovery_index[v] == lowlink_value[v]:
            component = []
            while stack[-1] != v:
                component.append(stack.pop())
            component.append(stack.pop())
            scc_list.append(component)

    for v in range(n):
        if not visited[v]:
            dfs(v)
    
    return scc_list

def calculate_edges_needed_to_make_strongly_connected(graph):
    strongly_connected_components = identify_strongly_connected_components(graph)
    
    component_graph = defaultdict(list)
    for component in strongly_connected_components:
        for node in component:
            for neighbor in graph[node]:
                if neighbor not in component:
                    component_graph[tuple(component)].append(tuple([neighbor for neighbor in strongly_connected_components if neighbor != component and set(neighbor).intersection(graph[node])]))

    root_component = None
    for comp in component_graph:
        if not component_graph[comp]:
            root_component = comp
            break
            
    if root_component is None:
        return -1
    
    return len(component_graph) - 1

# Тестирование
example_graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [4],
    4: []
}
edges_required = calculate_edges_needed_to_make_strongly_connected(example_graph)
print("Необходимо минимум", edges_required) # Должно быть: -1