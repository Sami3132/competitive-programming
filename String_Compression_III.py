class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        curr = word[0]
        ans = ""

        for i in range(len(word)):
            if word[i] == curr:
                if count == 9:
                    ans += f"{count}{curr}"
                    count = 0

                count += 1
            else:
                ans += f"{count}{curr}"
                curr = word[i]
                count = 1
        
        ans += f"{count}{curr}"

        return ans
