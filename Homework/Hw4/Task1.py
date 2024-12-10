from collections import deque

def find_shortest_path_with_all_keys(grid):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = None, None
    key_set = set()
    lock_set = set()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                start_x, start_y = r, c
            elif grid[r][c].islower():
                key_set.add(grid[r][c])
            elif grid[r][c].isupper():
                lock_set.add(grid[r][c])

    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start_x, start_y, 0, set())])
    visited = set([(start_x, start_y, '')])

    while queue:
        current_x, current_y, steps, acquired_keys = queue.popleft()

        if len(acquired_keys) == len(key_set):
            return steps

        for dx, dy in movements:
            next_x, next_y = current_x + dx, current_y + dy
            if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] != '#':
                updated_keys = acquired_keys.copy()
                if grid[next_x][next_y].islower():
                    updated_keys.add(grid[next_x][next_y])
                if grid[next_x][next_y].isupper():
                    if grid[next_x][next_y].lower() not in updated_keys:
                        continue 

                new_state = (next_x, next_y, ''.join(sorted(updated_keys)))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((next_x, next_y, steps + 1, updated_keys))

    return -1

# Тестирование
grid_example = [
    "@.a..",
    "###.#",
    "b.A.B"
]
result = find_shortest_path_with_all_keys(grid_example)
print("Минимальное количество шагов для сбора всех ключей:", result) # Должно быть: 8