from collections import deque, defaultdict

def largest_path_value(colors, connections):
    n = len(colors)
    
    graph = defaultdict(list)
    incoming_degree = [0] * n
    for start, end in connections:
        graph[start].append(end)
        incoming_degree[end] += 1
    
    sorted_order = []
    queue = deque(i for i in range(n) if incoming_degree[i] == 0)
    
    while queue:
        current_v = queue.popleft()
        sorted_order.append(current_v)
        for u in graph[current_v]:
            incoming_degree[u] -= 1
            if incoming_degree[u] == 0:
                queue.append(u)
    
    if len(sorted_order) < n:
        return -1
    
    dp = [[0] * 26 for _ in range(n)]

    for idx in range(n):
        dp[idx][ord(colors[idx]) - ord('a')] = 1
    
    for v in sorted_order:
        for u in graph[v]:
            for char_index in range(26):
                dp[u][char_index] = max(dp[u][char_index], 
                                                       dp[v][char_index] + (1 if char_index == ord(colors[u]) - ord('a') else 0))
    
    return max(max(row) for row in dp)

# Тестирование
colors_example = "abaca"
edges_example = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
result = largest_path_value(colors_example, edges_example)
print("Максимальное значение пути по цветам:", result) # Должно быть: 3