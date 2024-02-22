class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        nLeft = 0
        nRight = sum(nums)
        maxVal = nRight
        ans = [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                nLeft += 1
            else:
                nRight -= 1
            
            newVal = nLeft + nRight

            if newVal == maxVal:
                ans.append(i + 1)
                maxVal = newVal
            elif newVal > maxVal:
                ans = [i + 1]
                maxVal = newVal

        return ans
