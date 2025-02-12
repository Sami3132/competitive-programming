class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        myDict = dict()

        for i in range(n):
            num = nums[i]
            total = 0

            while num:
                total += num % 10
                num //= 10
            
            if total in myDict:
                if nums[i] >= myDict[total][0]:
                    myDict[total][1] = myDict[total][0]
                    myDict[total][0] = nums[i]
                elif nums[i] > myDict[total][1]:
                    myDict[total][1] = nums[i]
            else:
                myDict[total] = [nums[i], -1]
        
        ans = -1

        for key, val in myDict.items():
            if val[1] != -1:
                ans = max(ans, val[0] + val[1])
        
        return ans
