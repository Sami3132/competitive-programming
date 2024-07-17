class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= ind:
                ind = i

        return ind == 0
        
