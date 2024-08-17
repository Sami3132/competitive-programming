class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > target:
                    right -= 1
                else:
                    left += 1
                
                if abs(sum - target) < abs(ans - target):
                    ans = sum
        
        return ans
