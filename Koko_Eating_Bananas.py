class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            total = 0

            for pile in piles:
                total += ceil(pile / mid)
                
                if total > h:
                    break
            
            if total > h:
                left = mid + 1
            else:
                right = mid
        
        return right
