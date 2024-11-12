class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        result = []
        
        maximum = []
        currMax = 0
        
        for price, beauty in items:
            currMax = max(currMax, beauty)
            maximum.append((price, currMax))
        
        for query in queries:
            idx = bisect_right(maximum, (query, float('inf'))) - 1
            
            if idx >= 0:
                result.append(maximum[idx][1])
            else:
                result.append(0)
        
        return result
