class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        ans = 0

        while k > 0:
            num = -heappop(nums)

            if num == 1:
                ans += num * k
                break

            ans += num
            num = ceil(num / 3)
            heappush(nums, -num)
            k -= 1

        return ans
