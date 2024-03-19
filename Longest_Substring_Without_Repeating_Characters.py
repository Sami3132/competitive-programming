class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newSet = set()

        left = 0
        right = 0
        longest = 0

        while right < len(s):
            if s[right] not in newSet:
                newSet.add(s[right])
                right += 1
            else:
                longest = max(longest, right - left)
                newSet.discard(s[left])
                left += 1
            
        longest = max(longest, right - left)
        
        return longest
