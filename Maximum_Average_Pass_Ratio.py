class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passCount, totalCount):
            return (passCount + 1) / (totalCount + 1) - passCount / totalCount

        heap = []
        for passCount, totalCount in classes:
            heapq.heappush(heap, (-gain(passCount, totalCount), passCount, totalCount))
        
        for _ in range(extraStudents):
            negGain, passCount, totalCount = heapq.heappop(heap)
            passCount += 1
            totalCount += 1
            heapq.heappush(heap, (-gain(passCount, totalCount), passCount, totalCount))
        
        totalRatio = 0
        for _, passCount, totalCount in heap:
            totalRatio += passCount / totalCount
        
        return totalRatio / len(classes)
