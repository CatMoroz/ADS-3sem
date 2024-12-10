from collections import deque

def convert_maze(maze_input):
    maze = [list(line) for line in maze_input.strip().split('\n')]
    return maze

def breadth_first_search(start, maze):
    total_rows, total_cols = len(maze), len(maze[0])
    move_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance_map = [[float('inf')] * total_cols for _ in range(total_rows)]
    queue = deque([start])
    distance_map[start[0]][start[1]] = 0

    while queue:
        current_x, current_y = queue.popleft()
        for delta_x, delta_y in move_directions:
            next_x, next_y = current_x + delta_x, current_y + delta_y
            if 0 <= next_x < total_rows and 0 <= next_y < total_cols and maze[next_x][next_y] != '#':
                if distance_map[next_x][next_y] > distance_map[current_x][current_y] + 1:
                    distance_map[next_x][next_y] = distance_map[current_x][current_y] + 1
                    queue.append((next_x, next_y))
    return distance_map

def locate_meeting_point(a_distances, b_distances, f_position, maze):
    min_cost = float('inf')
    optimal_point = None

    total_rows, total_cols = len(maze), len(maze[0])

    for r in range(total_rows):
        for c in range(total_cols):
            if maze[r][c] == '.' or (r, c) == f_position:
                a_cost = a_distances[r][c]
                b_cost = b_distances[r][c]
                f_cost = a_distances[f_position[0]][f_position[1]]
                
                total_cost = (a_cost if a_cost < float('inf') else 0) + (b_cost if b_cost < float('inf') else 0) + f_cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    optimal_point = (r, c)

    return optimal_point

def trace_path(maze, start, end_point, distance_map):
    path_trace = []
    current_x, current_y = end_point
    
    while (current_x, current_y) != start:
        path_trace.append((current_x, current_y))
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x, next_y = current_x + delta_x, current_y + delta_y
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]):
                if distance_map[next_x][next_y] == distance_map[current_x][current_y] - 1:
                    current_x, current_y = next_x, next_y
                    break
    path_trace.append(start)
    return path_trace

def control_robots(maze_input):
    maze = convert_maze(maze_input)
    total_rows, total_cols = len(maze), len(maze[0])

    a_start = None
    b_start = None
    f_position = None

    for r in range(total_rows):
        for c in range(total_cols):
            if maze[r][c] == 'A':
                a_start = (r, c)
            elif maze[r][c] == 'B':
                b_start = (r, c)
            elif maze[r][c] == 'F':
                f_position = (r, c)

    a_distance_map = breadth_first_search(a_start, maze)
    b_distance_map = breadth_first_search(b_start, maze)

    meeting_point = locate_meeting_point(a_distance_map, b_distance_map, f_position, maze)

    if meeting_point:
        a_path_trace = trace_path(maze, a_start, meeting_point, a_distance_map)
        b_path_trace = trace_path(maze, b_start, meeting_point, b_distance_map)

        for x, y in a_path_trace:
            if maze[x][y] not in ('A', 'B', 'F'):
                maze[x][y] = 'o'
        for x, y in b_path_trace:
            if maze[x][y] not in ('A', 'B', 'F'):
                maze[x][y] = 'o'

        if meeting_point != f_position:
            mx, my = meeting_point
            maze[mx][my] = 'M'

    return '\n'.join(''.join(row) for row in maze)

# Тестирование
test_maze = """
######
#A...#
#....#
#..F.#
#B.#.#
######
"""

output_result = control_robots(test_maze)
print(output_result)