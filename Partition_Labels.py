class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)

        for i,c in enumerate(s):
            count[c] = i
        
        left = 0
        right = 0
        ans = []

        for i,c in enumerate(s):
            right = max(right, count[c])

            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        
        return ans
