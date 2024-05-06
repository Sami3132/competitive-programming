class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        st = deque()
        st2 = deque()
        i = 0
        ans = 0
        j = 0

        while i < len(nums):
            if not st or st[-1] >= nums[i]:
                st.append(nums[i])
            else:
                while st and st[-1] < nums[i]:
                    st.pop()

                st.append(nums[i])

            while st and st[0] > nums[i] + 2:
                while nums[j] != st[0]:
                    j+=1

                st.popleft()
                j+=1
            
            if not st2 or st2[-1] <= nums[i]:
                st2.append(nums[i])
            else:
                while st2 and st2[-1] > nums[i]:
                    st2.pop()
                    
                st2.append(nums[i])
            while st2 and st2[0] < nums[i] - 2:
                while nums[j] != st2[0]:
                    j+=1
                st2.popleft()
                j+=1
            ans += i-j+1
            i+=1

        return ans                
