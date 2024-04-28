class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_length = 1
        n = len(nums)

        increasing_q = collections.deque()
        decreasing_q = collections.deque() 

        for right in range(n):
            while increasing_q and increasing_q[-1] > nums[right]:
                increasing_q.pop()
            increasing_q.append(nums[right])
            
            while decreasing_q and decreasing_q[-1] < nums[right]:
                decreasing_q.pop()

            decreasing_q.append(nums[right]) 

            while decreasing_q[0] - increasing_q[0] > limit:
                if decreasing_q[0] == nums[left]:
                    decreasing_q.popleft()
                if increasing_q[0] == nums[left]:
                    increasing_q.popleft()
                
                left += 1

            max_length = max(max_length, right - left + 1)
            
        return max_length
        
