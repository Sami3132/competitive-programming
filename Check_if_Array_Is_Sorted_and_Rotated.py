class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3:
            return True
        
        if nums == sorted(nums):
            return True

        if nums[0] < nums[n - 1]:
            return False
        
        decreaseCount = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                decreaseCount += 1
            
            if decreaseCount == 2:
                return False
        
        return True
