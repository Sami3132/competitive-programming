class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        divi = len(nums) / 3
        output = []

        newDict = dict()

        for num in nums:
            if num in newDict:
                newDict[num] += 1
            else:
                newDict[num] = 1
        
        for count in newDict:
            if newDict[count] > divi:
                output.append(count)
        
        return output
