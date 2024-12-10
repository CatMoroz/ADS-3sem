from collections import deque

def escape_maze(maze_representation):
    grid = [list(r) for r in maze_representation.strip().split('\n')]
    total_rows, total_cols = len(grid), len(grid[0])
    
    movement_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start = None
    queue = deque()

    for r in range(total_rows):
        for c in range(total_cols):
            if grid[r][c] == 'S':
                start = (r, c)
                queue.append((r, c, []))
                break
        if start:
            break

    if not start:
        print("Starting point 'S' not found.")
        return grid

    explored_positions = set()
    explored_positions.add(start)

    while queue:
        current_x, current_y, current_path = queue.popleft()

        if current_x == 0 or current_x == total_rows - 1 or current_y == 0 or current_y == total_cols - 1:
            for path_x, path_y in current_path:
                if grid[path_x][path_y] == '.':
                    grid[path_x][path_y] = 'o'
            grid[start[0]][start[1]] = 'S'
            break

        for delta_x, delta_y in movement_directions:
            next_x, next_y = current_x + delta_x, current_y + delta_y
            if 0 <= next_x < total_rows and 0 <= next_y < total_cols and (next_x, next_y) not in explored_positions:
                if grid[next_x][next_y] in {'.', 'S'}:
                    explored_positions.add((next_x, next_y))
                    queue.append((next_x, next_y, current_path + [(current_x, current_y)]))

    for r in grid:
        print(''.join(r))

# Тестирование
maze_example = """
#####
#.S.#
###.#
#...#
#.###
"""
escape_maze(maze_example)