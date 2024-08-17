class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = points[0]

        for i in range(1, n):
            newDP = points[i]
            left, right = [0] * m, [0] * m

            left[0] = dp[0]

            for j in range(1, m):
                left[j] = max(dp[j], left[j - 1] - 1)

            right[m - 1] = dp[m - 1]

            for j in range(m - 2, -1, -1):
                right[j] = max(dp[j], right[j + 1] - 1)
            
            for j in range(m):
                newDP[j] += max(left[j], right[j])
        
            dp = newDP
        
        return max(dp)
