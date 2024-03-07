class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            minNum = i

            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minNum]:
                    minNum = j
            
            if minNum != i:
                nums[minNum], nums[i] = nums[i], nums[minNum]
