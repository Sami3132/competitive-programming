class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefixSum = [0] * len(nums)
        prefixSum[0] = 1

        for i in range(1, len(nums)):
            if nums[i] & 1 == nums[i - 1] & 1:
                prefixSum[i] = 1
            else:
                prefixSum[i] = prefixSum[i - 1] + 1
        
        ans = []

        for query in queries:
            if prefixSum[query[1]] >= query[1] - query[0] + 1:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
