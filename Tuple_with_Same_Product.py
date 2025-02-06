class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        myDict = defaultdict(int)
        count = 0

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                myDict[product] += 1

        for product in myDict:
            freq = myDict[product]
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8

        return count
