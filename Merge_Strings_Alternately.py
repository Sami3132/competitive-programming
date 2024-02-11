class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        new_word = ""

        for i in range(max_length):
            if i < len(word1):
                new_word += word1[i]
            if i < len(word2):
                new_word += word2[i]

        return new_word
