class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        left = 0
        right = len(nums) - 1
        pos = -1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                pos = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        ans[0] = pos

        left = 0
        right = len(nums) - 1
        pos = -1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                pos = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        ans[1] = pos

        return ans
