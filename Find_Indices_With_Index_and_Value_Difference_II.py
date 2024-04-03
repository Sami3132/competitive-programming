class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minNum = maxNum = -1 

        for i, x in enumerate(nums):
            if i >= indexDifference:
                if minNum == -1 or nums[i - indexDifference] < nums[minNum]:
                    minNum = i - indexDifference

                if maxNum == -1 or nums[i - indexDifference] > nums[maxNum]:
                    maxNum = i - indexDifference

                if x - nums[minNum] >= valueDifference:
                    return [minNum, i]

                if nums[maxNum] - x >= valueDifference:
                    return [maxNum, i]

        return [-1, -1]
