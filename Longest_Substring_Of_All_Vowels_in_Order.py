class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowel = 'aeiou'

        length = 0
        curr = 0
        ans = 0

        for el, group in groupby(word):
            if el == vowel[length]:
                curr += len(list(group))
                length += 1
                
                if length == 5:
                    ans = max(ans, curr)
                    curr = 0
                    length = 0
            elif el == vowel[0]:
                curr = len(list(group))
                length = 1
            else:
                curr = 0
                length = 0
        
        return ans
