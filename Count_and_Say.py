class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        word = self.countAndSay(n - 1)
        ans = ""
        firstChar = word[0]
        count = 1

        for i in range(1, len(word)):
            if word[i] == firstChar:
                count = count + 1
            else:
                ans = ans + str(count)
                ans = ans + str(firstChar)
                firstChar = word[i]
                count = 1

        ans = ans + str(count)
        ans = ans + str(firstChar)

        return ans
