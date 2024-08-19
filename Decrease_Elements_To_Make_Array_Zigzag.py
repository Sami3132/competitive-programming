class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        ans1 = ans2 = 0

        for i in range(1, len(nums), 2):
            if i == len(nums) - 1:
                if nums[i] >= nums[i - 1]:
                    ans1 += 1 + nums[i] - nums[i - 1]
            else:
                if nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]:
                    ans1 += 1 + nums[i] - min(nums[i - 1], nums[i + 1])

        for i in range(0, len(nums), 2):
            if i == 0:
                if nums[i] >= nums[i + 1]:
                    ans2 += 1 + nums[i] - nums[i + 1]
            elif i == len(nums) - 1:
                if nums[i] >= nums[i - 1]:
                    ans2 += 1 + nums[i] - nums[i - 1]
            else:
                if nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]:
                    ans2 += 1 + nums[i] - min(nums[i - 1], nums[i + 1])
        
        return min(ans1, ans2)
