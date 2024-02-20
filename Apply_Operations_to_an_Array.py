class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        output = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            if nums[i] == 0:
                zeroCount += 1
                continue
            
            output.append(nums[i])
        
        output.append(nums[-1])

        output.extend([0] * zeroCount)
        return output
