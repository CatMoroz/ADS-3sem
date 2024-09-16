def list_edge_to_list_sm(list_edge:list[tuple[int, int]], n) -> list[list[int]]:
    list_sm = [[] for _ in range(n)]
    for edge in list_edge:
        list_sm[edge[0]].append(edge[1])
    return list_sm

def clother(list_edge: list[tuple[int, int]], n) -> list[int]:
    list_sm = list_edge_to_list_sm(list_edge, n)
    visit = [0] * n
    ans = []
    def dfs(v:int):
        visit[v] = 1
        for u in list_sm[v]:
            if visit[u] == 0:
                dfs(u)
        ans.append(v)
    for i in range(n):
        if visit[i] == 0:
            dfs(i)
    ans.reverse()
    return ans

dict_cl = {0: 'Пиджак', 1: 'Часы', 2: 'Брюки', 3: 'Рубашка', 4: 'Трусы', 5: 'Носки', 6: 'Туфли', 7: 'Галстук', 8:'Ремень'}
list_edge = [(7, 0),(5, 6),(3, 8), (3, 7),
 (8, 0), (4, 2),(4, 6),(2, 6),
 (2, 8)]

res = clother(list_edge, 9)

for i in res:
    print(dict_cl[i])