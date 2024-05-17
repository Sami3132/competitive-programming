class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        left, right = k - 1, size - 1
        
        cuurPoint = sum(cardPoints[:k])
        maxPoint = cuurPoint
        
        for _ in range(k):
            cuurPoint += (cardPoints[right] - cardPoints[left])
            maxPoint = max(maxPoint, cuurPoint)
            
            left, right = left - 1, right - 1
            
        return maxPoint
