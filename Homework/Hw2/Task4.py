class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        visit = [0] * n

        def dfs(v: int):
            visit[v] = 1
            for i in range(n):
                if (isConnected[v][i] and not visit[i]):
                    dfs(i)

        for i in range(n):
            if (visit[i]):
                continue
            else:
                provinces += 1
                dfs(i)

        return provinces