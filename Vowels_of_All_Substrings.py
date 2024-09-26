class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(len(word)):
            if word[i] in vowels:
                count += (len(word) - i) * (i + 1)
        
        return count
