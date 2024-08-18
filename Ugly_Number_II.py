class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            nextNum = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(nextNum)

            if nextNum == nums[p2] * 2:
                p2 += 1
            if nextNum == nums[p3] * 3:
                p3 += 1
            if nextNum == nums[p5] * 5:
                p5 += 1
        
        return nums[n - 1]
