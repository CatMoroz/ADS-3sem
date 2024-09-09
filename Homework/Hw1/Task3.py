def if_two_direction_path(list_sm: list[list[int]], v: int, u: int) -> bool:
    one_dir_flg = False
    def dfs(v : int) -> None:
        color[v] = 1
        for u in list_sm[v]:
            if color[u] != 1: 
                dfs(u)
    
    color = [0]**len(list_sm)
    dfs(v)
    if color[u] == 1:
        one_dir_flg = True
    color = [0]**len(list_sm)
    dfs(u)
    if color[v] == 1:
        return True
    return False