class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        myDict = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in myDict:
                myDict[num] = myDict[sqrt] + 1
                res = max(res, myDict[num])
            else:
                myDict[num] = 1

        return res
