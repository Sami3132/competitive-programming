class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[len(nums) - 1]
        ans = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > last:
                times = nums[i] // last

                if nums[i] % last:
                    times += 1

                last = nums[i] // times
                ans += times - 1
            else:
                last = nums[i]
                
        return ans
