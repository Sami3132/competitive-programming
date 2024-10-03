class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        length = sum(nums)

        if length % p == 0:
            return 0

        rem = length % p
        myDict = { 0 : -1 }
        n = len(nums)
        cur, ans = 0, n

        for i,num in enumerate(nums):
            cur = (cur + num) % p

            if (cur - rem) % p in myDict:
                ans = min(ans, i - myDict[(cur - rem) % p])

            myDict[cur] = i

        return ans if ans < n else -1
