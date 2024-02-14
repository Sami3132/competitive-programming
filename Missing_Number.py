class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in newSet:
                return i
