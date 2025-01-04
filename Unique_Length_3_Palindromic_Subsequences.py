class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        left = set()
        right = Counter(s)

        for char in s:
            right[char] -= 1
            for el in left:
                if right[el] > 0:
                    ans.add((char, el))
        
            left.add(char)
        
        return len(ans)
