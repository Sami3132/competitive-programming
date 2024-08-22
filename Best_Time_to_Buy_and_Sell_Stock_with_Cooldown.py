class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        myDict = dict()

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in myDict:
                return myDict[(i, buying)]
            
            if buying:
                myDict[(i, buying)] = max(dfs(i + 1, not buying) - prices[i], dfs(i + 1, buying))
            else:
                myDict[(i, buying)] = max(dfs(i + 2, not buying) + prices[i], dfs(i + 1, buying))
            
            return myDict[(i, buying)]
        
        return dfs(0, True)
