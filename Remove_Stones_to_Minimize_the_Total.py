class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            current = -heapq.heappop(piles)
            current -= floor(current / 2)
            heapq.heappush(piles, -current)
        
        return abs(sum(piles))
