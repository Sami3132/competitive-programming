class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        heap = []
        count = 0

        while nums or len(heap) > 1:
            newNum = minNum = nextMin = 0

            if heap and (not nums or heap[0] < nums[-1]):
                minNum = heapq.heappop(heap)
            else:
                if nums:
                    minNum = nums.pop()
            
            if minNum >= k:
                return count
            
            if heap and (not nums or heap[0] < nums[-1]):
                nextMin = heapq.heappop(heap)
            else:
                if nums:
                    nextMin = nums.pop()
                else:
                    return count

            newNum = minNum * 2 + nextMin
            heapq.heappush(heap, newNum)
            count += 1
        
        return count
