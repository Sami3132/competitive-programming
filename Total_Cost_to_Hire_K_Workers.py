class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs) - 1
        heap1, heap2 = [], []

        total = 0

        for _ in range(k):
            while left <= right and len(heap1) < candidates:
                heapq.heappush(heap1, costs[left])
                left += 1
            while left <= right and len(heap2) < candidates:
                heapq.heappush(heap2, costs[right])
                right -= 1
            
            el1 = heap1[0] if heap1 else float('inf')
            el2 = heap2[0] if heap2 else float('inf')

            if el1 <= el2:
                total += el1
                heapq.heappop(heap1)
            else:
                total += el2
                heapq.heappop(heap2)
        
        return total
