class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum = sum(grid[0])
        bottomSum = 0

        ans = float("inf")

        for i in range(len(grid[0])):
            topSum -= grid[0][i]
            robotTwoSum = max(topSum, bottomSum)
            ans = min(ans, robotTwoSum)
            bottomSum += grid[1][i]
        
        return ans
