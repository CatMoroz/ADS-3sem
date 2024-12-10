class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_count = [[0, 0] for _ in range(n)]
        
        for relationship in trust:
            trust_count[relationship[0] - 1][0] += 1
            trust_count[relationship[1] - 1][1] += 1
            
        for p in range(n):
            if trust_count[p] == [0, n - 1]:
                return p + 1
        
        return -1