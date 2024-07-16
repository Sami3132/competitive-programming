class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k

        k = k - numOnes - numZeros
        if k <= 0:
            return numOnes

        return numOnes - k
