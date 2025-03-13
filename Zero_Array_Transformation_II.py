class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total = 0
        k = 0
        diffArr = [0] * (n + 1)

        for i in range(n):
            while total + diffArr[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                if right >= i:
                    diffArr[max(left, i)] += val
                    diffArr[right + 1] -= val

            total += diffArr[i]

        return kclass Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total = 0
        k = 0
        diffArr = [0] * (n + 1)

        for i in range(n):
            while total + diffArr[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                if right >= i:
                    diffArr[max(left, i)] += val
                    diffArr[right + 1] -= val

            total += diffArr[i]

        return k
