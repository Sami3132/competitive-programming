class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                max_count = max(max_count, counter)
                counter = 0
        
        return max(max_count, counter)
