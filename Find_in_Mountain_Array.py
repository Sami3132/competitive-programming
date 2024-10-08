# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        l, r = 1, length - 2

        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountain_arr.get(m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m

        l, r = 0, peak - 1

        while l <= r:
            m = (l + r) // 2
            el = mountain_arr.get(m)
            if target > el:
                l = m + 1
            elif target < el:
                r = m - 1
            else:
                return m
        
        l, r = peak, length - 1

        while l <= r:
            m = (l + r) // 2
            el = mountain_arr.get(m)

            if target < el:
                l = m + 1
            elif target > el:
                r = m - 1
            else:
                return m
    
        return -1
