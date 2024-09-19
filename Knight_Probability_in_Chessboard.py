class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        dp[row][column][0] = 1
        
        for move in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[nr][nc][move] += dp[r][c][move - 1] / 8
        
        total_probability = 0
        for r in range(n):
            for c in range(n):
                total_probability += dp[r][c][k]
        
        return total_probability
