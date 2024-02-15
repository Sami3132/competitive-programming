class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        myDict = dict()

        for i, el in enumerate(nums):
            myDict[el] = i
        
        for i, j in operations:
            ind = myDict[i]
            nums[ind] = j
            myDict.pop(i)
            myDict[j] = ind
        
        return nums
