class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        firstCounter = Counter(p)
        secondCounter = Counter(s[:len(p) - 1])
        anagramCount = []

        for i in range(len(p) - 1, len(s)):
            secondCounter[s[i]] += 1

            if firstCounter == secondCounter:
                anagramCount.append(i - len(p) + 1)

            secondCounter[s[i - len(p) + 1]] -= 1
            if secondCounter[s[i - len(p) + 1]] == 0:
                del secondCounter[s[i - len(p) + 1]]
        
        return anagramCount
