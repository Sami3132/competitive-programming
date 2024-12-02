class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = 1
        words = sentence.split(" ")
        n = len(searchWord)

        for word in words:
            if n <= len(word):
                if word[: n] == searchWord:
                    return ans
            
            ans += 1

        print(words)
        return -1
