class Solution:
    def totalFruit(self, tree):
        r, nums, res = 0, defaultdict(int), 0

        for i in range(len(tree)):
            nums[tree[i]] += 1
            while len(nums) > 2:
                nums[tree[r]] -= 1 
                if not nums[tree[r]]:
                    nums.pop(tree[r])
                r += 1
            res = max(res, i - r + 1)
        return res
