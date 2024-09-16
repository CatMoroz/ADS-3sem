def topological_sort(list_sm: list[list[int]], n: int):
    visit = [0] * n
    queue = list(range(n))
    result = []

    while (len(queue) != 0):
        current = queue[0]
        if (visit[current]):
            queue.pop(0)
            continue
        if (all(map(lambda x: visit[x], list_sm[current]))):
            visit[current] = 1
            result.insert(0, queue.pop(0))
        else:
            queue = list_sm[current] + queue

    return result