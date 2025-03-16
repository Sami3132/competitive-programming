class Solution:
    def maximumCandies(self, candies, k):
        maxCandies = 0

        for candy in candies:
            maxCandies = max(maxCandies, candy)

        left = 0
        right = maxCandies

        while left < right:
            middle = (left + right + 1) // 2

            if self.allocateCandies(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left

    def allocateCandies(self, candies, k, numCandies):
        maxNum = 0

        for pile in candies:
            maxNum += pile // numCandies

        return maxNum >= k
