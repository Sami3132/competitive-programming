class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] -= i
        
        myDict = defaultdict(int)

        for i in range(n):
            myDict[nums[i]] += 1
        
        totalPair = (n * (n - 1)) // 2
        
        for val in myDict.values():
            if val > 1:
                totalPair -= (val * (val - 1)) // 2
        
        return totalPair
