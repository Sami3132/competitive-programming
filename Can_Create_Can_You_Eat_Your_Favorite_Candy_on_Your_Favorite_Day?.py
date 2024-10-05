class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []

        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        
        print(candiesCount)
        
        for t, d, c in queries:
            lastDay = candiesCount[t] - 1
            firstDay = candiesCount[t - 1] // c if t > 0 else 0

            ans.append(firstDay <= d <= lastDay)
        
        return ans
