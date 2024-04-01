class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        total = 0
        sum = 0

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                sum += 1
            
            total += sum
        
        return total
