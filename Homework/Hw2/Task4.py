class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        province_count = 0
        n = len(isConnected)
        visited = [0] * n

        def dfs(v: int):
            visited[v] = 1
            for u in range(n):
                if isConnected[v][u] and not visited[u]:
                    dfs(u)

        for v in range(n):
            if visited[v]:
                continue
            else:
                province_count += 1
                dfs(v)

        return province_count