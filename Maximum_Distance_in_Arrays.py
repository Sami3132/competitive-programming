class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum = []
        maximum = deque()

        for i in range(len(arrays)):
            bisect.insort(minimum, [arrays[i][0], i])

            if len(minimum) > 2:
                minimum.pop()
            
            bisect.insort(maximum, [arrays[i][-1], i])

            if len(maximum) > 2:
                maximum.popleft()
        
        if minimum[0][1] != maximum[-1][1]:
            return maximum[-1][0] - minimum[0][0]
        
        return max(maximum[-2][0] - minimum[0][0], maximum[-1][0] - minimum[1][0])
