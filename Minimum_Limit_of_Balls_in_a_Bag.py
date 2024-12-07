class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def calc(n):
            operations = 0

            for el in nums:
                operations += ceil(el / n) - 1

                if operations > maxOperations:
                    return False
            
            return True
        
        l, r = 1, max(nums)

        while l < r:
            m = l + ((r - l) // 2)

            if calc(m):
                r = m
            else:
                l = m + 1
        
        return l
