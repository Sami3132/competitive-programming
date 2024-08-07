class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs) // 2
        ans = 0

        for i in range(n):
            ans += costs[i][0]
        
        for i in range(n, n * 2):
            ans += costs[i][1]
        
        return ans
