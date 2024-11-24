class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        minimum = float("inf")
        neg = 0

        for row in matrix:
            for el in row:
                ans += abs(el)
                minimum = min(minimum, abs(el))

                if el < 0:
                    neg += 1
        
        if neg % 2:
            ans -= 2 * minimum
        
        return ans
