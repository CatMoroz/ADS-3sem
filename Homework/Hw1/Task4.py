class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        out_in = [[0, 0] for _ in range(n)]
        for edge in trust:
            out_in[edge[0] - 1][0] += 1
            out_in[edge[1] - 1][1] += 1
        for i in range(n):
            if out_in[i] == [0, n - 1]:
                return i + 1
        return -1