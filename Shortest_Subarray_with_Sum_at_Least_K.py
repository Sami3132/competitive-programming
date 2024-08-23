class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        total = 0
        ans = float("inf")
        dq = deque()

        for i in range(len(nums)):
            total += nums[i]

            if total >= k:
                ans = min(ans, i + 1)
            
            while dq and total - dq[0][0] >= k:
                ans = min(ans, i - dq.popleft()[1])
            
            while dq and total <= dq[-1][0]:
                dq.pop()
            
            dq.append((total, i))
        
        return -1 if ans == float("inf") else ans
