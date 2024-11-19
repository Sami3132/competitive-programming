from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        total = 0
        ans = 0
        uniqueCount = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1
            total += nums[i]

            if freq[nums[i]] == 1:
                uniqueCount += 1

            if i >= k:
                left_num = nums[i - k]
                total -= left_num
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    uniqueCount -= 1

            if uniqueCount == k:
                ans = max(ans, total)

        return ans
