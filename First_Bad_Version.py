# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        ans = -1

        while first <= last:
            mid = first + ((last - first) // 2)

            if isBadVersion(mid):
                ans = mid
                last = mid - 1
            else:
                first = mid + 1
    
        return ans
